/**
 * Tantra Gyan Vedic Astrology Book - Progressive Web App Service Worker
 * Version: 1.0.1
 * 
 * Features:
 * - Instant offline access for all 3 editions (Bilingual, Hindi, English)
 * - Explicit one-click offline download with real-time progress reporting
 * - Automated version tracking & instant "Update Available" notification
 * - Seamless zero-downtime cache invalidation & atomic updates
 * - Dynamic font caching for Google Fonts
 * - Stale-While-Revalidate for HTML pages, Cache-First for static assets
 */

const APP_VERSION = '1.0.1';
const CACHE_NAME = `tantragyan-v${APP_VERSION}`;
const FONT_CACHE_NAME = 'tantragyan-fonts-v1.0';

// Critical core assets and all 3 editions to cache for complete offline functioning
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
  'manifest.webmanifest',
  'manifest.json'
];

// 1. Install Event: Pre-cache assets and signal waiting state if updating
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return Promise.allSettled(
        PRECACHE_ASSETS.map((asset) =>
          cache.add(asset).catch((err) => {
            console.warn(`[ServiceWorker v${APP_VERSION}] Pre-cache skipped for ${asset}:`, err);
          })
        )
      );
    }).then(() => {
      // Notify clients of new version availability
      return self.clients.matchAll().then((clients) => {
        clients.forEach((client) => {
          client.postMessage({ type: 'UPDATE_AVAILABLE', version: APP_VERSION });
        });
      });
    })
  );
});

// 2. Activate Event: Clean up any old version caches and claim all clients
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

// 3. Fetch Event: Multi-tier caching
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
  // Strategy: Stale-While-Revalidate with instant offline fallback
  if (request.mode === 'navigate' || request.headers.get('accept')?.includes('text/html')) {
    event.respondWith(
      caches.open(CACHE_NAME).then((cache) => {
        return cache.match(request).then((cachedResponse) => {
          const fetchPromise = fetch(request).then((networkResponse) => {
            if (networkResponse && networkResponse.status === 200) {
              cache.put(request, networkResponse.clone());
            }
            return networkResponse;
          }).catch(() => {
            // Network failure / Offline mode
            if (cachedResponse) return cachedResponse;
            // Fallback to index.html if specific page isn't in cache
            return cache.match('index.html') || cache.match('./');
          });

          return cachedResponse || fetchPromise;
        });
      })
    );
    return;
  }

  // C. Static Local Assets (CSS, JS, SVG, Images, Favicon, Manifest)
  // Strategy: Cache-First with network refresh
  if (url.origin === self.location.origin) {
    event.respondWith(
      caches.open(CACHE_NAME).then((cache) => {
        return cache.match(request).then((cachedResponse) => {
          if (cachedResponse) {
            // Optional background refresh for CSS and JS
            if (request.url.includes('.css') || request.url.includes('.js')) {
              fetch(request).then((networkResponse) => {
                if (networkResponse && networkResponse.status === 200) {
                  cache.put(request, networkResponse.clone());
                }
              }).catch(() => {});
            }
            return cachedResponse;
          }

          // Not in cache: fetch from network, then cache
          return fetch(request).then((networkResponse) => {
            if (networkResponse && networkResponse.status === 200) {
              cache.put(request, networkResponse.clone());
            }
            return networkResponse;
          }).catch((err) => {
            console.warn(`[ServiceWorker] Failed to fetch asset: ${request.url}`, err);
          });
        });
      })
    );
    return;
  }

  // Default: Network with Cache Fallback
  event.respondWith(
    caches.match(request).then((cachedResponse) => {
      return cachedResponse || fetch(request);
    })
  );
});

// 4. Message Event: Full offline download with progress & version management
self.addEventListener('message', async (event) => {
  if (!event.data) return;

  // A. Trigger full offline download with live progress reporting
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
          await cache.add(asset);
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
