# VOX: German Language Learning App

A simple, interactive web app to help users learn German through flashcards, number counting, and an AI-based translation assistant.

## 🔧 Tech Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (DB Browser for SQLite)
- **AI Feature**: OpenAI API (for translations)
- **Local Tunneling (Optional)**: Ngrok

---

## 🚀 Features

- ✅ **German Counting Module**: Learn to count in German (1–10, 1–20, etc.)
- ✅ **Flashcards**: Interactive flashcards to memorize German vocabulary.
- ✅ **AI Translator**: Translate text between English and German using AI.
- ✅ **Quiz Module**: Answer multiple-choice questions to test your knowledge.
- ✅ **Score Table**: View your score and correct/incorrect answers after quiz completion.
- ✅ **Retake Option**: Option to retake the quiz to improve learning.
- ✅ **Simple UI**: Designed for ease of use and accessibility.

---

## 🖥️ How to Run the App (WSL / Linux)

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/german-language-app.git
cd german-language-app
```

### 2. Set up virtual environment (optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Export Flask environment variable
```bash
export FLASK_APP=app.py
export FLASK_ENV=production  # or development for debug mode
```

### 5. Run the Flask app (no auto-reload)
```bash
flask run --host=0.0.0.0 --port=5000
```

or:

```bash
python3 app.py
```

---

## 🌐 Accessing Locally or via Ngrok (Optional)

To access your app from a mobile device or share it:
1. [Download Ngrok](https://ngrok.com/download) and install it.
2. In terminal:
```bash
ngrok http 5000
```
3. Copy the **Forwarding URL** and open it in your browser.

---

## 🧠 Quiz & Database

- Questions and options are stored in `fuck.db` using SQLite.
- Use **DB Browser for SQLite** to edit or view the quiz data.
- Sample schema includes:
  - `questions (id INT, question TEXT)`
  - `options (id INT, question_id INT, option_text TEXT, is_correct INT)`

---

## 💬 Feedback or Contributions

Feel free to fork the project or create pull requests. Feedback is always welcome!

---

