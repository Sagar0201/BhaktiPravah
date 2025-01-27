document.addEventListener('click', (event) => {
     const menuIdPrefix = 'menu-list';
     const infoIdPrefix = 'info-';

     if (event.target.id.startsWith(menuIdPrefix)) {
          // Hide all info containers
          document.querySelectorAll('.info-desc').forEach(info => info.style.display = 'none');

          // Show the corresponding info container
          const infoId = infoIdPrefix + event.target.id.split(menuIdPrefix)[1];
          document.getElementById(infoId).style.display = 'block';

          // Set the text of info-title
          document.getElementById('info-title').textContent = event.target.textContent.trim();

          // Hide the menu container
          document.getElementById('menu').style.display = 'none';

          // Show the info-container
          document.querySelector('.info-container').style.display = 'block';

     } else if (event.target.id === 'back-btn') {
          // Hide the info-container
          document.querySelector('.info-container').style.display = 'none';

          // Show the menu container
          document.getElementById('menu').style.display = 'flex';
     } else if (event.target.id === 'add-count') {
          updateCounter(1);
     } else if (event.target.id === 'sub-count') {
          updateCounter(-1);
     } else if (event.target.id === 'reset-count') {
          updateCounter(0, true);
     }
});

function updateCounter(change, reset = false) {
     const counterElement = document.getElementById('counter-value');
     let counter = parseInt(counterElement.textContent);

     if (reset) {
          counter = 0;
     } else {
          counter = (counter + change + 109) % 109;
     }

     counterElement.textContent = counter;
     playTone(counter);
     navigator.vibrate([100, 50, 100, 50, 200]); // Short vibration

}

function playTone(counter) {
     const tone = document.getElementById('tone');

     switch (counter) {
          case 11:
          case 21:
          case 51:
          case 108:
               tone.play();
               break;
     }
}






const defaultFontSize = parseFloat(getComputedStyle(document.documentElement).fontSize); // Root font size (1em)
const maxFontSize = 2; // Maximum size in em
const minFontSize = 1; // Minimum size in em

document.getElementById("fontSizeBtn").addEventListener("click", () => {
     const pElements = document.querySelectorAll('.info-desc p');

     pElements.forEach((pElement) => {
          let currentSize = parseFloat(window.getComputedStyle(pElement).fontSize) /
               defaultFontSize; // Convert px to em

          // Increase size or reset to minimum size
          if (currentSize < maxFontSize) {
               pElement.style.fontSize = (currentSize + 0.1).toFixed(1) +
                    'em'; // Increment by 0.1em
          } else {
               pElement.style.fontSize = minFontSize + 'em'; // Reset to 1em
          }
     });
});




function updateCounter(change, reset = false) {
     const counterElement = document.getElementById('counter-value');
     let counter = parseInt(counterElement.textContent);

     if (reset) {
          counter = 0;
     } else {
          counter = (counter + change + 109) % 109;
     }

     // Update the counter in the DOM
     counterElement.textContent = counter;

     // Save the counter value to localStorage
     localStorage.setItem('counter', counter);

     // Play tone and vibrate
     playTone(counter);
     navigator.vibrate([100, 50, 100, 50, 200]); // Short vibration
}


document.addEventListener('DOMContentLoaded', () => {
     const storedCounter = localStorage.getItem('counter');
     const counterElement = document.getElementById('counter-value');
     counterElement.textContent = storedCounter !== null ? storedCounter : 0;
});