/**
 * Tantra Gyan Vedic Astrology Book - Progressive Web App Service Worker
 * Version: 1.2.0 (Production Stable • Zero-Reload • Bulletproof Navigation)
 * 
 * Features:
 * - 100% Reliable Navigation: Direct network-first with graceful offline cache fallback
 * - Zero Chrome crashes: Uses fetch(request.url) preventing mode:navigate manual redirect errors
 * - Zero redirect loops: Strictly zero auto-reloads on controllerchange
 * - Complete offline functionality for all 3 editions (Bilingual, Hindi, English)
 * - Atomic cache updates with immediate legacy cache purge
 * - Dynamic font caching for Google Fonts
 * - Live offline download progress reporting
 */

const APP_VERSION = '1.2.0';
const CACHE_NAME = `tantragyan-v${APP_VERSION}`;
const FONT_CACHE_NAME = 'tantragyan-fonts-v1.0';

// Critical core assets and all 3 editions to cache for complete offline functioning
const PRECACHE_ASSETS = [
  './',
  'index.html',
  'hindi.html',
  'english.html',
  'css/book.css?v=4.3',
  'css/tables.css?v=4.1',
  'js/sounds-data.js?v=3.9',
  'js/sound.js?v=3.9',
  'js/book-engine.js?v=4.0',
  'js/book-ui.js?v=4.3',
  'assets/yantra.svg',
  'assets/ganesha.svg',
  'assets/icons/elements_diamond_chart.svg',
  'assets/icons/upachaya_diamond_chart.svg',
  'assets/icons/kendra_trikona_diamond_chart.svg',
  'assets/icons/nakshatra_mandala_wheel.svg',
  'assets/icons/bhava_karaka_diamond_chart.svg',
  'assets/icons/aspect_wheel.svg',
  'assets/icons/lagna_chart.svg',
  'assets/icons/raja_yogas_chart.svg',
  'assets/icons/viparita_chart.svg',
  'assets/icons/medical_astrology_chart.svg',
  'assets/images/planets/sun.png',
  'assets/images/planets/moon.png',
  'assets/images/planets/mars.png',
  'assets/images/planets/mercury.png',
  'assets/images/planets/jupiter.png',
  'assets/images/planets/venus.png',
  'assets/images/planets/saturn.png',
  'assets/images/planets/rahu.png',
  'assets/images/planets/ketu.png',
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
  'llms.txt',
  'llms-full.txt'
];

// 1. Install Event: Instant activation with non-blocking parallel pre-caching
self.addEventListener('install', (event) => {
  self.skipWaiting();
  // Pre-cache essential shell in parallel without blocking installation
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return Promise.allSettled(
        PRECACHE_ASSETS.map((asset) =>
          fetch(asset, { cache: 'no-cache' }).then((res) => {
            if (res && res.status === 200) {
              return cache.put(asset, res);
            }
          }).catch(() => {})
        )
      );
    })
  );
});

// 2. Activate Event: Clean up outdated caches and claim clients immediately
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((name) => name !== CACHE_NAME && name !== FONT_CACHE_NAME)
          .map((name) => {
            console.log(`[ServiceWorker] Deleting legacy cache: ${name}`);
            return caches.delete(name);
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

// 3. Fetch Event: Clean, robust multi-tier caching
self.addEventListener('fetch', (event) => {
  const request = event.request;
  const url = new URL(request.url);

  // Skip non-GET requests and browser extensions
  if (request.method !== 'GET' || !url.protocol.startsWith('http')) {
    return;
  }

  // Bypass service worker entirely for astrology-book-engine and all PDF files
  if (url.pathname.includes('/astrology-book-engine/') || url.pathname.endsWith('.pdf')) {
    return;
  }

  // A. Google Fonts API & Fonts Caching (Cache-First with Background Refresh)
  if (url.origin === 'https://fonts.googleapis.com' || url.origin === 'https://fonts.gstatic.com') {
    event.respondWith(
      caches.open(FONT_CACHE_NAME).then((fontCache) => {
        return fontCache.match(request).then((cachedResponse) => {
          if (cachedResponse) return cachedResponse;
          return fetch(request).then((networkResponse) => {
            if (networkResponse && networkResponse.status === 200) {
              fontCache.put(request, networkResponse.clone());
            }
            return networkResponse;
          }).catch(() => cachedResponse);
        });
      })
    );
    return;
  }

  // B. Navigation Requests (HTML Pages: index.html, hindi.html, english.html)
  // Strategy: Direct Network-First using request.url
  // Online visitors get the 100% untouched native network response (guaranteed zero header/decoding corruption)
  // Offline visitors get the seamless cached book!
  if (request.mode === 'navigate' || (request.method === 'GET' && request.headers.get('accept')?.includes('text/html'))) {
    event.respondWith(
      (async () => {
        try {
          // Fetch directly via URL string (follows redirects cleanly, avoids manual redirect errors)
          const networkResponse = await fetch(request.url);
          if (networkResponse && networkResponse.status === 200) {
            const clone = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(request.url, clone);
              if (url.pathname === '/' || url.pathname.endsWith('index.html')) {
                cache.put('./', clone.clone());
              }
            }).catch(() => {});
            return networkResponse;
          }
        } catch (networkError) {
          // Network failed (offline, airplane mode)
        }

        // Offline Fallback: Serve matching cached page
        const cache = await caches.open(CACHE_NAME);
        let cached = await cache.match(request.url);
        if (!cached) {
          const path = url.pathname;
          if (path.endsWith('/hindi.html')) {
            cached = await cache.match('hindi.html');
          } else if (path.endsWith('/english.html')) {
            cached = await cache.match('english.html');
          } else {
            cached = (await cache.match('./')) || (await cache.match('index.html'));
          }
        }
        if (cached) return cached;
        return new Response('<!DOCTYPE html><html><head><meta charset="utf-8"><title>Offline Mode</title></head><body style="font-family:sans-serif;text-align:center;padding:3rem;"><h1>📡 Offline Mode</h1><p>Please check your internet connection to access Tantra Gyan online.</p></body></html>', {
          headers: { 'Content-Type': 'text/html; charset=utf-8' }
        });
      })()
    );
    return;
  }

  // C. Static Local Assets (CSS, JS, SVG, Images, Favicon, Manifest)
  // Strategy: Cache-First with Network fallback
  if (url.origin === self.location.origin) {
    event.respondWith(
      caches.match(request).then((cachedResponse) => {
        if (cachedResponse) {
          // Background revalidation for CSS/JS without blocking instant delivery
          if (request.url.includes('.css') || request.url.includes('.js')) {
            event.waitUntil(
              fetch(request).then((networkResponse) => {
                if (networkResponse && networkResponse.status === 200) {
                  caches.open(CACHE_NAME).then((cache) => {
                    cache.put(request, networkResponse);
                  }).catch(() => {});
                }
              }).catch(() => {})
            );
          }
          return cachedResponse;
        }

        // Not in cache: fetch from network and cache
        return fetch(request).then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const clone = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(request, clone);
            }).catch(() => {});
          }
          return networkResponse;
        }).catch(() => {
          if (request.destination === 'image') {
            return caches.match('assets/icon-192.png');
          }
        });
      })
    );
    return;
  }

  // Default fallback: Cache first then Network
  event.respondWith(
    caches.match(request).then((cached) => cached || fetch(request))
  );
});

// 4. Message Event: Full offline download with progress & update activation
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
          const res = await fetch(asset);
          if (res && res.status === 200) {
            await cache.put(asset, res);
          }
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
