/**
 * Tantra Gyan Vedic Astrology Book - Service Worker Clean-up & Migration
 * Version: 1.3.0 (Zero Worker Redirects • 100% Native Browser Navigation)
 * 
 * Purpose:
 * Completely unregisters any active service worker and purges legacy caches
 * to eliminate 100% of web worker redirects, reload loops, and Chrome navigation errors.
 */

self.addEventListener('install', (event) => {
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    self.registration.unregister().then(() => {
      return caches.keys().then((cacheNames) => {
        return Promise.all(cacheNames.map((name) => caches.delete(name)));
      });
    }).then(() => {
      return self.clients.claim();
    })
  );
});

// Zero interception: NEVER call event.respondWith!
// Allows the browser to handle all network navigations natively with zero worker redirects.
self.addEventListener('fetch', (event) => {
  return;
});
