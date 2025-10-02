from flask import Flask, request, jsonify, render_template
from gradio_client import Client

app = Flask(__name__)
client = Client("Wizard1971/Aatma")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    try:
        result = client.predict(
            message=user_input,
            system_message="You are a friendly Chatbot.",
            max_tokens=512,
            temperature=0.7,
            top_p=0.95,
            api_name="/chat"
        )
        return jsonify({"reply": result})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')