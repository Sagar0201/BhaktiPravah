const CACHE_NAME = "bhaktipravah-cache-v2";
const urlsToCache = [
     "/",
     "/static/css/style.css",
     "/static/js/app.js",
     "/static/icons/icon-192x192.png",
     "/static/icons/icon-512x512.png",
     "/static/manifest.json"
];

// Install event - Cache basic assets
self.addEventListener("install", (event) => {
     event.waitUntil(
          caches.open(CACHE_NAME)
          .then((cache) => {
               console.log("✅ Caching app shell");
               return cache.addAll(urlsToCache);
          })
     );
});

// Fetch event - Dynamic caching for media files
self.addEventListener("fetch", (event) => {
     event.respondWith(
          caches.match(event.request).then((cachedResponse) => {
               if (cachedResponse) {
                    return cachedResponse;
               }

               return fetch(event.request).then((networkResponse) => {
                    // Cache only media files (images, audio, video)
                    if (event.request.url.match(/\.(jpg|jpeg|png|gif|mp3|mp4|ogg|webm)$/)) {
                         return caches.open(CACHE_NAME).then((cache) => {
                              cache.put(event.request, networkResponse.clone());
                              return networkResponse;
                         });
                    }

                    return networkResponse;
               }).catch(() => {
                    // Fallback if media is not cached
                    if (event.request.url.match(/\.(jpg|jpeg|png|gif)$/)) {
                         return caches.match("/static/images/offline-placeholder.jpg");
                    }
                    if (event.request.url.match(/\.(mp3|mp4|ogg|webm)$/)) {
                         return caches.match("/static/media/offline-audio.mp3");
                    }
               });
          })
     );
});

// Activate event - Cleanup old caches
self.addEventListener("activate", (event) => {
     event.waitUntil(
          caches.keys().then((cacheNames) => {
               return Promise.all(
                    cacheNames.filter((name) => name !== CACHE_NAME)
                    .map((name) => caches.delete(name))
               );
          })
     );
});