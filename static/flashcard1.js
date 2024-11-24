document.addEventListener("DOMContentLoaded", function() {
    const flashcards = document.querySelectorAll('.flashcard');
    let currentIndex = 0;

    // Toggle flip for each flashcard
    flashcards.forEach(flashcard => {
        flashcard.addEventListener('click', function() {
            flashcard.classList.toggle('flipped');
        });
    });

    // Get buttons for previous and next navigation
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');

    // Add logic to show next and previous flashcards
    prevBtn.addEventListener('click', function() {
        if (currentIndex > 0) {
            currentIndex--;
            showFlashcard(currentIndex);
        }
    });

    nextBtn.addEventListener('click', function() {
        if (currentIndex < flashcards.length - 1) {
            currentIndex++;
            showFlashcard(currentIndex);
        }
    });

    // Function to update visible flashcard
    function showFlashcard(index) {
        flashcards.forEach((flashcard, i) => {
            if (i === index) {
                flashcard.style.display = 'flex';
            } else {
                flashcard.style.display = 'none';
            }
        });
    }

    // Show the first flashcard initially
    showFlashcard(currentIndex);
});
