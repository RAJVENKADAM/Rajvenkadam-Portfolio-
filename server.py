# server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from bot import ask_bot  # Import your bot function
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow frontend to make requests to this server

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        if not data or "question" not in data:
            return jsonify({"error": "No question provided"}), 400

        question = data["question"].strip()
        if not question:
            return jsonify({"error": "Empty question"}), 400

        # Call the bot function
        answer = ask_bot(question)

        # Ensure answer is string
        if isinstance(answer, list) and len(answer) > 0:
            answer = answer[0].get("generated_text", "Sorry, I am unable to respond right now.")
        elif isinstance(answer, dict):
            answer = answer.get("generated_text", "Sorry, I am unable to respond right now.")
        else:
            answer = str(answer)

        return jsonify({"answer": answer})

    except Exception as e:
        print("Backend error:", e)
        return jsonify({"answer": "Sorry, I am unable to respond right now."}), 500

if __name__ == "__main__":
    print("🤖 Chatbot server running on http://localhost:5000")
    app.run(host="0.0.0.0", port=5000)
