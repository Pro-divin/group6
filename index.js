// Assuming that you have the same basic structure as before for navigating through images

// Get all the items and buttons
const items = document.querySelectorAll('.carousel .list .item');
const prevButton = document.getElementById('prev');
const nextButton = document.getElementById('next');
const firstButton = document.getElementById('first');
const lastButton = document.getElementById('last');
let currentIndex = 0; // Track the current index of the displayed image

// Function to update the carousel based on the current index
function updateCarousel() {
    items.forEach((item, index) => {
        if (index === currentIndex) {
            item.style.display = 'block';  // Show the current item
        } else {
            item.style.display = 'none';   // Hide the other items
        }
    });
}

// Initialize carousel display
updateCarousel();

// Previous button click event
prevButton.addEventListener('click', () => {
    if (currentIndex > 0) {
        currentIndex--;
        updateCarousel();
    }
});

// Next button click event
nextButton.addEventListener('click', () => {
    if (currentIndex < items.length - 1) {
        currentIndex++;
        updateCarousel();
    }
});

// First button click event
firstButton.addEventListener('click', () => {
    currentIndex = 0;  // Set index to first image
    updateCarousel();
});

// Last button click event
lastButton.addEventListener('click', () => {
    currentIndex = items.length - 1;  // Set index to last image
    updateCarousel();
});
