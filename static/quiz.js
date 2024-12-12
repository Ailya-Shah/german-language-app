let currentQuestionIndex = 0;  // Track the current question

// Start the quiz by showing the first question
function startQuiz() {
    // Hide the start button
    document.getElementById('start-button').style.display = 'none';

    // Show the first question
    showQuestion(currentQuestionIndex);
}

// Show the question based on the index
function showQuestion(index) {
    const questions = document.querySelectorAll('.question');
    const question = questions[index];

    if (question) {
        // Show the current question
        question.style.display = 'block';
    }
}

// Handle answer selection
function selectAnswer(questionIndex, selectedOptionId) {
    // Send the selected answer to the backend if needed
    // For now, we just log the selected option
    console.log('Selected option:', selectedOptionId);

    // Hide the current question
    document.getElementById('question-' + questionIndex).style.display = 'none';

    // Move to the next question
    currentQuestionIndex++;

    // Show the next question
    showQuestion(currentQuestionIndex);
}

// Optional: Show the results after the quiz is completed
function showResults() {
    document.getElementById('result').innerText = 'Quiz Completed!';  // Show results message
}

