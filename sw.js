/**
 * Tantra Gyan Vedic Astrology Book - Progressive Web App Service Worker
 * Version: 1.0.3
 * 
 * Features:
 * - Safari / iOS WebKit Redirection Fix (eliminates WebKitErrorDomain 100)
 * - 100% Instant offline access for all 3 editions (Bilingual, Hindi, English)
 * - Zero-action auto pre-caching: just visiting once caches entire book in browser
 * - Works completely offline in browser without needing to install an app
 * - Explicit one-click offline download with real-time percentage progress reporting
 * - Automated version tracking & instant "Update Available" notification
 * - Seamless zero-downtime cache invalidation & atomic updates
 * - Dynamic font caching for Google Fonts
 * - Stale-While-Revalidate with instant 0ms sanitized offline cache return for HTML pages
 */

const APP_VERSION = '1.0.3';
const CACHE_NAME = `tantragyan-v${APP_VERSION}`;
const FONT_CACHE_NAME = 'tantragyan-fonts-v1.0';

// Critical core assets and all 3 editions to cache for complete offline functioning
// Note: manifest.json is excluded from precache because it 301-redirects to manifest.webmanifest
const PRECACHE_ASSETS = [
  './',
  'index.html',
  'hindi.html',
  'english.html',
  'css/book.css?v=3.8',
  'css/tables.css?v=3.8',
  'js/sounds-data.js?v=3.8',
  'js/sound.js?v=3.8',
  'js/book-engine.js?v=3.8',
  'js/book-ui.js?v=3.8',
  'assets/yantra.svg',
  'assets/ganesha.svg',
  'assets/icon-192.png',
  'assets/icon-512.png',
  'assets/icon-maskable-192.png',
  'assets/icon-maskable-512.png',
  'assets/apple-touch-icon.png',
  'assets/favicon-32.png',
  'assets/favicon-16.png',
  'assets/og-image.jpg',
  'favicon.ico',
  'manifest.webmanifest'
];

/**
 * Safari (iOS & macOS WebKit) Redirection Fix:
 * WebKit strictly blocks service workers from returning responses where response.redirected === true,
 * throwing "Response served by ServiceWorker has redirections".
 * This helper reconstructs a pristine Response object, stripping all internal redirect metadata.
 */
async function cleanResponse(response) {
  if (!response) return response;
  if (response.redirected) {
    const body = await response.blob();
    return new Response(body, {
      status: response.status || 200,
      statusText: response.statusText || 'OK',
      headers: response.headers
    });
  }
  return response;
}

/**
 * Safely fetches and caches an asset, ensuring any redirected response
 * is sanitized before being written into CacheStorage.
 */
async function safeCachePut(cache, requestOrUrl, response) {
  if (!response || (response.status !== 200 && response.type !== 'opaque')) return;
  const toCache = response.redirected
    ? new Response(await response.clone().blob(), {
        status: response.status,
        statusText: response.statusText,
        headers: response.headers
      })
    : response.clone();
  await cache.put(requestOrUrl, toCache);
}

// 1. Install Event: Pre-cache assets immediately with redirection sanitization
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(async (cache) => {
      for (const asset of PRECACHE_ASSETS) {
        try {
          const res = await fetch(asset);
          await safeCachePut(cache, asset, res);
        } catch (err) {
          console.warn(`[ServiceWorker v${APP_VERSION}] Pre-cache skipped for ${asset}:`, err);
        }
      }
    }).then(() => {
      // Force immediate activation so first-time visitors have 100% offline access immediately
      return self.skipWaiting();
    })
  );
});

// 2. Activate Event: Clean up old version caches and claim all clients immediately
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME && cacheName !== FONT_CACHE_NAME) {
            console.log(`[ServiceWorker] Removing legacy cache: ${cacheName}`);
            return caches.delete(cacheName);
          }
        })
      );
    }).then(() => {
      return self.clients.claim();
    }).then(() => {
      return self.clients.matchAll().then((clients) => {
        clients.forEach((client) => {
          client.postMessage({ type: 'VERSION_ACTIVATED', version: APP_VERSION });
        });
      });
    })
  );
});

// 3. Fetch Event: Multi-tier caching with Safari Redirection Sanitization
self.addEventListener('fetch', (event) => {
  const request = event.request;
  const url = new URL(request.url);

  // Skip non-GET requests and browser extensions
  if (request.method !== 'GET' || !url.protocol.startsWith('http')) {
    return;
  }

  // A. Google Fonts API & Fonts Caching (Stale-While-Revalidate / Cache-First)
  if (url.origin === 'https://fonts.googleapis.com' || url.origin === 'https://fonts.gstatic.com') {
    event.respondWith(
      caches.open(FONT_CACHE_NAME).then((fontCache) => {
        return fontCache.match(request).then((cachedResponse) => {
          const fetchPromise = fetch(request).then((networkResponse) => {
            if (networkResponse && networkResponse.status === 200) {
              fontCache.put(request, networkResponse.clone());
            }
            return networkResponse;
          }).catch(() => null);

          return cachedResponse || fetchPromise;
        });
      })
    );
    return;
  }

  // B. Navigation Requests (HTML Pages: index.html, hindi.html, english.html)
  // Strategy: Instant 0ms Sanitized Cache Return with background network update.
  // 100% Safari & iOS WebKit redirection-safe!
  if (request.mode === 'navigate' || request.headers.get('accept')?.includes('text/html')) {
    event.respondWith(
      (async () => {
        const cache = await caches.open(CACHE_NAME);

        // Match requested URL or fallback to edition
        let cached = await cache.match(request);
        if (!cached) {
          const path = url.pathname;
          if (path === '/' || path.endsWith('/index.html')) {
            cached = (await cache.match('index.html')) || (await cache.match('./'));
          } else if (path.includes('hindi')) {
            cached = await cache.match('hindi.html');
          } else if (path.includes('english')) {
            cached = await cache.match('english.html');
          }
        }

        // Background network revalidation
        const networkPromise = fetch(request).then(async (netResponse) => {
          if (netResponse && netResponse.status === 200) {
            await safeCachePut(cache, request, netResponse);
            if (url.pathname === '/' || url.pathname.endsWith('index.html')) {
              await safeCachePut(cache, './', netResponse);
            }
          }
          return netResponse;
        }).catch((err) => {
          return null;
        });

        // If cached page is available, return sanitized clean response immediately!
        if (cached) {
          event.waitUntil(networkPromise);
          return cleanResponse(cached);
        }

        // If not in cache yet, await network
        const netRes = await networkPromise;
        if (netRes) return cleanResponse(netRes);

        // Ultimate offline fallback to index.html
        const fallback = (await cache.match('index.html')) || (await cache.match('./'));
        if (fallback) return cleanResponse(fallback);

        return new Response('<h1>Offline</h1><p>Tantra Gyan is unavailable offline at this moment.</p>', {
          headers: { 'Content-Type': 'text/html; charset=utf-8' }
        });
      })()
    );
    return;
  }

  // C. Static Local Assets (CSS, JS, SVG, Images, Favicon, Manifest)
  // Strategy: Cache-First with ignoreSearch fallback, background revalidation & redirect sanitization
  if (url.origin === self.location.origin) {
    event.respondWith(
      (async () => {
        const cache = await caches.open(CACHE_NAME);
        let cachedResponse = await cache.match(request);
        if (!cachedResponse) {
          cachedResponse = await cache.match(request, { ignoreSearch: true });
        }

        if (cachedResponse) {
          // Optional background refresh for CSS and JS
          if (request.url.includes('.css') || request.url.includes('.js')) {
            event.waitUntil(
              fetch(request).then(async (networkResponse) => {
                if (networkResponse && networkResponse.status === 200) {
                  await safeCachePut(cache, request, networkResponse);
                }
              }).catch(() => {})
            );
          }
          return cleanResponse(cachedResponse);
        }

        // Not in cache: fetch from network, then cache
        try {
          const networkResponse = await fetch(request);
          if (networkResponse && networkResponse.status === 200) {
            await safeCachePut(cache, request, networkResponse);
          }
          return cleanResponse(networkResponse);
        } catch (err) {
          if (request.destination === 'image') {
            const fallbackImg = await cache.match('assets/icon-192.png');
            if (fallbackImg) return cleanResponse(fallbackImg);
          }
          console.warn(`[ServiceWorker] Asset fetch failed offline: ${request.url}`);
        }
      })()
    );
    return;
  }

  // Default: Cache first then Network fallback
  event.respondWith(
    caches.match(request).then(async (cachedResponse) => {
      if (cachedResponse) return cleanResponse(cachedResponse);
      const netRes = await fetch(request);
      return cleanResponse(netRes);
    })
  );
});

// 4. Message Event: Full offline download with progress & version management
self.addEventListener('message', async (event) => {
  if (!event.data) return;

  // A. Trigger full offline download with live progress reporting & redirect sanitization
  if (event.data.action === 'DOWNLOAD_ALL_OFFLINE') {
    const source = event.source;
    const broadcastMsg = async (msg) => {
      if (source && source.postMessage) {
        source.postMessage(msg);
      }
      try {
        const clients = await self.clients.matchAll();
        for (const client of clients) {
          if (!source || client.id !== source.id) {
            client.postMessage(msg);
          }
        }
      } catch (e) {}
    };

    try {
      const cache = await caches.open(CACHE_NAME);
      const total = PRECACHE_ASSETS.length;

      for (let i = 0; i < total; i++) {
        const asset = PRECACHE_ASSETS[i];
        try {
          const res = await fetch(asset);
          await safeCachePut(cache, asset, res);
        } catch (err) {
          console.warn(`[ServiceWorker] Download skipped for ${asset}:`, err);
        }
        await broadcastMsg({
          type: 'DOWNLOAD_PROGRESS',
          current: i + 1,
          total: total,
          percent: Math.round(((i + 1) / total) * 100),
          item: asset
        });
      }

      await broadcastMsg({
        type: 'DOWNLOAD_COMPLETE',
        version: APP_VERSION
      });
    } catch (err) {
      await broadcastMsg({ type: 'DOWNLOAD_ERROR', error: err.message });
    }
  }

  // B. Apply update: activate new waiting service worker
  if (event.data.action === 'APPLY_UPDATE' || event.data.action === 'skipWaiting') {
    self.skipWaiting();
    if (event.source) {
      event.source.postMessage({ type: 'UPDATE_APPLIED', version: APP_VERSION });
    }
  }

  // C. Query current running version
  if (event.data.action === 'GET_VERSION') {
    if (event.source) {
      event.source.postMessage({ type: 'VERSION_INFO', version: APP_VERSION });
    }
  }
});
