from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flashcard1')
def flashcard1():
    return render_template('flashcard1.html')

@app.route('/flashcard2')
def flashcard2():
    return render_template('flashcard2.html')

if __name__ == '__main__':
    app.run(debug=True)
