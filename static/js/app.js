let deferredPrompt;

document.addEventListener("DOMContentLoaded", () => {
     // Register the service worker
     if ("serviceWorker" in navigator) {
          navigator.serviceWorker.register("/static/service-worker.js")
               .then(() => console.log("✅ Service Worker Registered"))
               .catch(err => console.error("❌ Service Worker Registration Failed:", err));
     }

     // Listen for the beforeinstallprompt event
     window.addEventListener("beforeinstallprompt", (event) => {
          console.log("📢 beforeinstallprompt event fired");

          // Prevent automatic prompt
          event.preventDefault();

          // Store the event for later use
          deferredPrompt = event;

          // Show the install button
          document.getElementById("install-button").style.display = "block";
     });

     // Install button click event
     document.getElementById("install-button").addEventListener("click", () => {
          if (deferredPrompt) {
               deferredPrompt.prompt();

               deferredPrompt.userChoice.then((choiceResult) => {
                    if (choiceResult.outcome === "accepted") {
                         console.log("✅ User accepted the install prompt");
                    } else {
                         console.log("❌ User dismissed the install prompt");
                    }
                    deferredPrompt = null; // Reset the prompt
               });
          }
     });

     // Check if PWA is already installed
     window.addEventListener("appinstalled", () => {
          console.log("🎉 PWA Installed Successfully");
          document.getElementById("install-button").style.display = "none"; // Hide button after install
     });
});