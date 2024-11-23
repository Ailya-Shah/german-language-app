document.addEventListener('DOMContentLoaded', function() {
    // Mapping of numbers to their German spellings
    const germanNumbers = {
        1: 'eins',
        2: 'zwei',
        3: 'drei',
        4: 'vier',
        5: 'fünf',
        6: 'sechs',
        7: 'sieben',
        8: 'acht',
        9: 'neun',
        10: 'zehn',
        11: 'elf',
        12: 'zwölf',
        13: 'dreizehn',
        14: 'vierzehn',
        15: 'fünfzehn',
        16: 'sechzehn',
        17: 'siebzehn',
        18: 'achtzehn',
        19: 'neunzehn',
        20: 'zwanzig',
        21: 'einundzwanzig',
        22: 'zweiundzwanzig',
        23: 'dreiundzwanzig',
        24: 'vierundzwanzig',
        25: 'fünfundzwanzig',
        26: 'sechsundzwanzig',
        27: 'siebenundzwanzig',
        28: 'achtundzwanzig',
        29: 'neunundzwanzig',
        30: 'dreißig',
        31: 'einunddreißig',
        32: 'zweiunddreißig',
        33: 'dreiunddreißig',
        34: 'vierunddreißig',
        35: 'fünfunddreißig',
        36: 'sechsunddreißig',
        37: 'siebenunddreißig',
        38: 'achtunddreißig',
        39: 'neununddreißig',
        40: 'vierzig',
        41: 'einundvierzig',
        42: 'zweiundvierzig',
        43: 'dreiundvierzig',
        44: 'vierundvierzig',
        45: 'fünfundvierzig',
        46: 'sechsundvierzig',
        47: 'siebenundvierzig',
        48: 'achtundvierzig',
        49: 'neunundvierzig',
        50: 'fünfzig'
    };

    // Select all grid items (number boxes)
    const gridItems = document.querySelectorAll('.grid-item');

    // Add click event to each grid item
    gridItems.forEach(function(item) {
        item.addEventListener('click', function() {
            const number = parseInt(item.querySelector('.number').innerText);  // Get the number clicked
            const translation = germanNumbers[number];  // Get the German translation for that number

            // Find the translation container and set its text
            const translationDiv = item.querySelector('.translation-text');
            if (translationDiv) {
                translationDiv.innerText = translation;  // Update translation text
                translationDiv.classList.add('show-translation');  // Show the translation
            }
        });
    });
});

