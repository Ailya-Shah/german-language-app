import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    # Render the index.html page
    return render_template('index.html')

# Define the route for translation
@app.route('/translate', methods=['POST'])
def translate():
    # Get the text input from the form in index.html
    text_to_translate = request.form.get('text_to_translate')

    # Set up the MyMemory API URL
    api_url = 'https://api.mymemory.translated.net/get'

    # Prepare the parameters for the API request
    params = {
        'q': text_to_translate,  # The text to translate
        'langpair': 'en|de'      # Source language (English) and target language (German)
    }

    # Send the API request
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        # Extract the translation from the API response
        translation = response.json()['responseData']['translatedText']
    else:
        translation = "Error: Unable to fetch translation"

    # Render the results in the same template (or a new one)
    return render_template('index.html', translation=translation)

if __name__ == '__main__':
    app.run(debug=True)

