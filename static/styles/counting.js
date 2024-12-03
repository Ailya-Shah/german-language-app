const countingCards = document.querySelectorAll('.counting-card');

countingCards.forEach(card => {
    card.addEventListener('click', () => {
        // Add custom behavior here, like playing a sound
        console.log('Card touched!');
    });
});
