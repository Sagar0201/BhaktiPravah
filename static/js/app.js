var deferredPrompt; // Use var to prevent redeclaration errors

document.addEventListener("DOMContentLoaded", () => {
     // Register the service worker
     if ("serviceWorker" in navigator) {
          navigator.serviceWorker.register("/static/service-worker.js")
               .then(() => console.log("✅ Service Worker Registered"))
               .catch(err => console.error("❌ Service Worker Registration Failed:", err));
     }

     // Listen for beforeinstallprompt event
     window.addEventListener("beforeinstallprompt", (event) => {
          console.log("📢 beforeinstallprompt event fired");

          event.preventDefault();
          deferredPrompt = event; // Store the event

          // Show the install button
          const installButton = document.getElementById("install-button");
          if (installButton) installButton.style.display = "block";
     });

     // Install button click event
     const installButton = document.getElementById("install-button");
     if (installButton) {
          installButton.addEventListener("click", () => {
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
     }

     // Hide install button after successful installation
     window.addEventListener("appinstalled", () => {
          console.log("🎉 PWA Installed Successfully");
          if (installButton) installButton.style.display = "none";
     });
});