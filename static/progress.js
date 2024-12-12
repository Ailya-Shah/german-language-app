document.addEventListener('DOMContentLoaded', () => {
    fetch('/progress/1') // Static user for demo
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('progress-container');
            data.forEach(entry => {
                const div = document.createElement('div');
                div.innerHTML = `
                    <p>Question: ${entry.question}</p>
                    <p>Selected Option: ${entry.selected_option}</p>
                    <p>Correct: ${entry.is_correct ? 'Yes' : 'No'}</p>
                    <p>Timestamp: ${entry.timestamp}</p>
                `;
                container.appendChild(div);
            });
        });
});
