from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data['text']
    source = data['from']
    target = data['to']

    api_url = "https://libretranslate.de/translate"
    payload = {
        "q": text,
        "source": source,
        "target": target,
        "format": "text"
    }

    try:
        response = requests.post(api_url, json=payload)
        result = response.json()
        return jsonify({"translatedText": result["translatedText"]})
    except Exception as e:
        return jsonify({"translatedText": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
