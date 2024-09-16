from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "your-openai-api-key"

@app.route('/api/generate', methods=['POST'])
def generate_text():
    data = request.get_json()
    prompt = data['prompt']

    # Call OpenAI API with the provided prompt
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT engine name
        prompt=prompt,
        max_tokens=100
    )

    generated_text = response.choices[0].text.strip()
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

openai.api_key = "your-openai-api-key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate_text():
    data = request.get_json()
    prompt = data['prompt']

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )

    generated_text = response.choices[0].text.strip()
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)
