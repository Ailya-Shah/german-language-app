import requests
import sqlite3
from flask import Flask, render_template, request, g

app = Flask(__name__)
DATABASE = 'fuck.db'

@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/translate', methods=['POST', 'GET'])
def translate():
    if request.method == 'POST':
        text_to_translate = request.form.get('text_to_translate')
        api_url = 'https://api.mymemory.translated.net/get'
        params = {'q': text_to_translate, 'langpair': 'en|de'}
        response = requests.get(api_url, params=params)

        translation = "Error: Unable to fetch translation"
        if response.status_code == 200:
            translation = response.json()['responseData']['translatedText']

        return render_template('index.html', translation=translation)

    return render_template('index.html', translation=None)

@app.route('/counting')
def counting():
    return render_template('counting.html')

@app.route('/flashcards')
def flashcards():
    return render_template('flashcards.html')  

@app.route('/flashcards/basic')
def flashcards_basic():
    return render_template('basic.html') 

@app.route('/flashcards/advanced')
def flashcards_advanced():
    return render_template('advanced.html')  

@app.route('/flashcards/verbs')
def flashcards_verbs():
    return render_template('verbs.html')  

@app.route('/cities')
def cities():
    return render_template('german.html')

@app.route('/books', methods=['GET'])
def books():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()


    cursor.execute("SELECT id, title, author, published_year, genre FROM books")
    books_data = cursor.fetchall()

    conn.close()


    print("Books Data:", books_data)

    return render_template('books.html', books=books_data)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()
print("Database connected:", DATABASE)

@app.route('/submit-quiz', methods=['POST'])
def submit_quiz():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    score = 0
    questions = cursor.execute("SELECT id FROM questions").fetchall()

    for question_id, in questions:
        selected_option = request.form.get(f"question_{question_id}")
        if selected_option:
            is_correct = cursor.execute("SELECT is_correct FROM options WHERE id = ?", (selected_option,)).fetchone()
            if is_correct and is_correct[0]:
                score += 1

    conn.close()

    return render_template('quiz_result.html', score=score, total=len(questions))

@app.route('/quiz')
def quiz():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Fetch questions and their options from the database
    questions = cursor.execute("SELECT id, question_text FROM questions").fetchall()
    question_data = []
    for question in questions:
        question_id = question[0]
        options = cursor.execute("SELECT id, option_text FROM options WHERE question_id = ?", (question_id,)).fetchall()
        question_data.append({
            'question_id': question_id,
            'question_text': question[1],
            'options': options
        })

    conn.close()

    return render_template('quiz.html', question_data=question_data)


if __name__ == '__main__':
    app.run(debug=True)











