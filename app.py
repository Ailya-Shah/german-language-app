import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Define the route for the splash screen (this will show splash.html)
@app.route('/')
def splash():
    return render_template('splash.html')


# Define the route for translation
@app.route('/translate', methods=['POST', 'GET'])
def translate():
    if request.method == 'POST':
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
        return render_template('index.html', translation=translation)

    # GET request (initial visit to the translation page)
    return render_template('index.html', translation=None)


# Route for German Counting page
@app.route('/counting')
def counting():
    return render_template('counting.html')  # You can create counting.html for this page

# Route for Flashcards page
@app.route('/flashcards')
def flashcards():
    return render_template('flashcards.html')  # You can create flashcards.html for this page


if __name__ == '__main__':
    app.run(debug=True)


