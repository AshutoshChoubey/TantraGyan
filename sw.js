/**
 * Tantra Gyan Vedic Astrology Book - Progressive Web App Service Worker
 * Version: 2.0.0 (Production Master • Zero-Redirect • Native Navigation Architecture)
 * 
 * Features:
 * - 100% Zero-Redirect Guarantee: Online navigations bypass worker proxying natively
 * - Complete Offline Protection: Seamless offline fallback when internet is disconnected
 * - Automatic Cache Migration: Purges all legacy caches (v1.x) upon activation
 * - Live Background Download: Smooth multi-asset caching with percentage reporting
 * - Dynamic Google Fonts Caching: Offline typography support for Vedic Devanagari fonts
 */

const APP_VERSION = '2.1.0';
const CACHE_NAME = `tantragyan-v${APP_VERSION}`;
const FONT_CACHE_NAME = 'tantragyan-fonts-v2.1';

// Critical core assets and editions for complete offline functioning
// Uses './' instead of 'index.html' to prevent Cloudflare 307 canonical redirects
const PRECACHE_ASSETS = [
  './',
  'hindi.html',
  'english.html',
  'css/book.css?v=5.0',
  'css/tables.css?v=5.0',
  'js/sounds-data.js?v=5.0',
  'js/sound.js?v=5.0',
  'js/book-engine.js?v=5.0',
  'js/book-ui.js?v=5.0',
  'assets/yantra.svg',
  'assets/ganesha.svg',
  'assets/icons/elements_diamond_chart.svg',
  'assets/icons/upachaya_diamond_chart.svg',
  'assets/icons/kendra_trikona_diamond_chart.svg',
  'assets/icons/nakshatra_mandala_wheel.svg',
  'assets/icons/bhava_karaka_diamond_chart.svg',
  'assets/icons/kalpurush_bhavas_diamond_chart.svg',
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

// 1. Install Event: Fast activation with non-blocking parallel pre-caching
self.addEventListener('install', (event) => {
  self.skipWaiting();
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

// 2. Activate Event: Wipe legacy caches (v1.x) and claim all clients immediately
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((name) => name !== CACHE_NAME && name !== FONT_CACHE_NAME)
          .map((name) => {
            console.log(`[ServiceWorker v${APP_VERSION}] Deleting legacy cache: ${name}`);
            return caches.delete(name);
          })
      );
    }).then(() => self.clients.claim())
  );
});

// 3. Fetch Event: Clean multi-tier caching with zero navigation redirects
self.addEventListener('fetch', (event) => {
  const request = event.request;
  const url = new URL(request.url);

  // Skip non-GET requests and external protocols
  if (request.method !== 'GET' || !url.protocol.startsWith('http')) {
    return;
  }

  // Bypass service worker entirely for book engine build artifacts and PDF downloads
  if (url.pathname.includes('/astrology-book-engine/') || url.pathname.endsWith('.pdf')) {
    return;
  }

  // A. Google Fonts API & Static Font Assets (Cache-First)
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

  // B. Top-Level Navigation Requests (HTML Pages)
  // STRICT ARCHITECTURAL INVARIANT:
  // When online, NEVER call event.respondWith() on navigation requests!
  // Allowing native browser network navigation guarantees:
  // 1. Zero Worker Redirects in Chromium & Safari
  // 2. Zero 307 redirect recursion loops
  // 3. Zero Content-Encoding mismatches
  // 4. Instant native page rendering
  if (request.mode === 'navigate') {
    if (self.navigator.onLine !== false) {
      return; // 100% Native browser pass-through!
    }

    // OFFLINE ONLY: Serve from CacheStorage when network is disconnected
    event.respondWith(
      (async () => {
        const cache = await caches.open(CACHE_NAME);
        const path = url.pathname;
        let cached = null;
        if (path.endsWith('hindi.html')) {
          cached = await cache.match('hindi.html');
        } else if (path.endsWith('english.html')) {
          cached = await cache.match('english.html');
        } else {
          cached = (await cache.match('./')) || (await cache.match('/'));
        }
        if (cached) return cached;
        return new Response(
          '<!DOCTYPE html><html><head><meta charset="utf-8"><title>Offline</title></head><body style="font-family:sans-serif;text-align:center;padding:3rem;"><h1>📡 Offline Mode</h1><p>Please connect to the internet to access Tantra Gyan online.</p></body></html>',
          { headers: { 'Content-Type': 'text/html; charset=utf-8' } }
        );
      })()
    );
    return;
  }

  // C. Local Static Assets (CSS, JS, SVG, Images, Favicon, Manifest)
  // Strategy: Cache-First with Network fallback
  if (url.origin === self.location.origin) {
    event.respondWith(
      caches.match(request).then((cachedResponse) => {
        if (cachedResponse) {
          return cachedResponse;
        }
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

// 4. Message Event: Background offline download with progress reporting
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
          const res = await fetch(asset, { cache: 'no-cache' });
          if (res && res.status === 200) {
            await cache.put(asset, res);
          }
        } catch (err) {
          console.warn(`[ServiceWorker v${APP_VERSION}] Download skipped for ${asset}:`, err);
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

  // B. Query current running version
  if (event.data.action === 'GET_VERSION') {
    if (event.source) {
      event.source.postMessage({ type: 'VERSION_INFO', version: APP_VERSION });
    }
  }
});
