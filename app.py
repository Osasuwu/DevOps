from flask import Flask, request, jsonify
from gpt4all import GPT4All

app = Flask(__name__)
model = GPT4All('orca-mini-3b-gguf2-q4_0.gguf')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    with model.chat_session():
        response = model.generate(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)

