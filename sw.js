/**
 * Tantra Gyan Vedic Astrology Book - Progressive Web App Service Worker
 * Version: 2.2.0 (User-Controlled Offline Architecture • Zero Navigation Conflict)
 * 
 * Features:
 * - Pure Online First: Regular web visitors run natively with ZERO service worker overhead
 * - User-Controlled Opt-In: Service worker activates ONLY when user explicitly downloads offline edition
 * - Seamless Multi-Page Offline: Serves cached editions (/hindi, /english, ./) without page reloads or loops
 * - Dynamic Google Fonts Caching: Vedic typography cached for offline reading
 * - Complete Self-Purging: Clean cache wiping when user disables offline mode or updates edition
 */

const APP_VERSION = '4.0.0';
const CACHE_NAME = `tantragyan-v${APP_VERSION}`;
const FONT_CACHE_NAME = 'tantragyan-fonts-v4.0';

// Essential assets for complete offline functioning
const PRECACHE_ASSETS = [
  './',
  'reader.html',
  'book.html',
  'bhrigu-nandi-nadi.html',
  'bnn.html',
  'bnn-reader.html',
  'tantra-sadhana-siddhi.html',
  'sadhana-reader.html',
  'hindi',
  'english',
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
  'assets/icons/sadhana_altar_mandala.svg',
  'assets/icons/sadhana_timeline_clock.svg',
  'assets/icons/sadhana_health_emergency_matrix.svg',
  'assets/icons/sadhana_samput_architecture.svg',
  'assets/icons/sadhana_panchakshari_125k_wheel.svg',
  'assets/icons/sadhana_lifestyle_disciplines_chart.svg',
  'assets/icons/elements_diamond_chart.svg',
  'assets/icons/purushartha_diamond_chart.svg',
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
  'assets/icons/deeptadi_sun_diamond_chart.svg',
  'assets/icons/navamsha_diamond_chart.svg',
  'assets/icons/bnn_philosophy_hierarchy_chart.svg',
  'assets/icons/bnn_directional_diamond_chart.svg',
  'assets/icons/bnn_jeeva_flow_diamond_chart.svg',
  'assets/icons/bnn_kartari_flank_diamond_chart.svg',
  'assets/icons/bnn_karaka_relationship_wheel.svg',
  'assets/icons/bnn_elemental_directional_diamond_chart.svg',
  'assets/icons/bnn_jeeva_12bhavas_diamond_chart.svg',
  'assets/icons/bnn_major_conjunctions_diamond_chart.svg',
  'assets/icons/bnn_triplet_rajyogas_diamond_chart.svg',
  'assets/icons/bnn_progression_paryaya_chart.svg',
  'assets/icons/bnn_bhrigu_bindu_diagram.svg',
  'assets/icons/bnn_protocol_flowchart.svg',
  'assets/icons/bnn_vakri_parivartana_chart.svg',
  'assets/icons/bnn_career_matrix_chart.svg',
  'assets/icons/bnn_marriage_matrix_chart.svg',
  'assets/icons/bnn_special_yogas_diamond_chart.svg',
  'assets/icons/bnn_rahu_ketu_nodal_axis_chart.svg',
  'assets/icons/bnn_transits_activation_chart.svg',
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

// 1. Install Event: Instant activation without blocking network
self.addEventListener('install', (event) => {
  self.skipWaiting();
});

// 2. Activate Event: Wipe legacy caches and claim clients cleanly
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((name) => name !== CACHE_NAME && name !== FONT_CACHE_NAME)
          .map((name) => {
            console.log(`[ServiceWorker v${APP_VERSION}] Purging legacy cache: ${name}`);
            return caches.delete(name);
          })
      );
    }).then(() => self.clients.claim())
  );
});

// 3. Fetch Event: Clean handling with zero navigation conflict
self.addEventListener('fetch', (event) => {
  const request = event.request;
  const url = new URL(request.url);

  // Skip non-GET requests and non-http protocols
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

  // B. Navigation Requests (HTML Pages: /, /hindi, /english, index.html, hindi.html, english.html)
  // Strategy: Network-First with Immediate Cache Fallback.
  // Guarantees:
  // - Online visitors get instant native server responses (zero 307 loops, zero worker redirects)
  // - Offline visitors seamlessly get their cached book pages without error screens
  if (request.mode === 'navigate') {
    event.respondWith(
      fetch(request)
        .then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const clone = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(request.url, clone);
              if (url.pathname === '/' || url.pathname === '') {
                cache.put('./', networkResponse.clone());
              }
            }).catch(() => {});
          }
          return networkResponse;
        })
        .catch(async () => {
          // Device is completely offline: Serve matched cached edition
          const cache = await caches.open(CACHE_NAME);
          const pathname = url.pathname;
          let cached = null;

          if (pathname.includes('hindi')) {
            cached = (await cache.match('hindi')) || (await cache.match('hindi.html')) || (await cache.match('/hindi'));
          } else if (pathname.includes('english')) {
            cached = (await cache.match('english')) || (await cache.match('english.html')) || (await cache.match('/english'));
          } else if (pathname.includes('reader') || pathname.includes('book')) {
            cached = (await cache.match('reader.html')) || (await cache.match('book.html')) || (await cache.match(request.url));
          } else {
            cached = (await cache.match('./')) || (await cache.match('index.html')) || (await cache.match('/')) || (await cache.match(request.url));
          }

          if (cached) return cached;

          // Generic friendly offline fallback
          return new Response(
            '<!DOCTYPE html><html lang="hi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ऑफ़लाइन मोड • Tantra Gyan</title><style>body{font-family:sans-serif;text-align:center;padding:3rem 1.5rem;background:#fdfbf7;color:#78350f}h1{font-size:1.6rem;color:#b45309}p{color:#57534e;max-width:480px;margin:1rem auto;line-height:1.6}a{display:inline-block;margin-top:1rem;padding:0.75rem 1.5rem;background:#b45309;color:#fff;text-decoration:none;border-radius:8px;font-weight:bold}</style></head><body><h1>📡 ऑफ़लाइन मोड (Offline Mode)</h1><p>यह पृष्ठ अभी कैश्ड नहीं है या इंटरनेट कनेक्शन उपलब्ध नहीं है। कृपया इंटरनेट से जुड़ने पर पुनः प्रयास करें।</p><a href="./">मुख्य पृष्ठ पर जाएं (Go Home)</a></body></html>',
            { headers: { 'Content-Type': 'text/html; charset=utf-8' } }
          );
        })
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
        });
      }).catch(() => {
        if (request.destination === 'image') {
          return caches.match('assets/icon-192.png');
        }
        return new Response('', { status: 408, statusText: 'Resource not available offline' });
      })
    );
    return;
  }
});

// 4. Message Event: User-Triggered Offline Download & Cache Management
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
            await cache.put(asset, res.clone());
            // Mirror clean URL variants to guarantee 100% offline match
            if (asset === 'hindi') {
              await cache.put('hindi.html', res.clone());
            } else if (asset === 'english') {
              await cache.put('english.html', res.clone());
            } else if (asset === './') {
              await cache.put('/', res.clone());
              await cache.put('index.html', res.clone());
            }
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

  // B. Clean cache deletion when user switches back to Online Only
  if (event.data.action === 'CLEAR_OFFLINE_CACHE') {
    try {
      await caches.delete(CACHE_NAME);
      await caches.delete(FONT_CACHE_NAME);
      const clients = await self.clients.matchAll();
      for (const client of clients) {
        client.postMessage({ type: 'CACHE_CLEARED' });
      }
    } catch (e) {}
  }

  // C. Query current running version
  if (event.data.action === 'GET_VERSION') {
    if (event.source) {
      event.source.postMessage({ type: 'VERSION_INFO', version: APP_VERSION });
    }
  }
});
