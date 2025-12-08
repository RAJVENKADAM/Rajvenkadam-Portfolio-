from flask import Flask, request, jsonify
from flask_cors import CORS
from bot import ask_bot  # Import your existing bot function

app = Flask(__name__)
CORS(app)  # Allow frontend to call this server

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        # Call your bot function
        answer = ask_bot(question)

        # Ensure answer is a string
        if isinstance(answer, list) and len(answer) > 0:
            # For Groq responses returned as list of dicts
            answer = answer[0].get("generated_text", "Sorry, I cannot answer right now.")
        elif isinstance(answer, dict):
            answer = answer.get("generated_text", "Sorry, I cannot answer right now.")
        else:
            answer = str(answer)

        return jsonify({"answer": answer})

    except Exception as e:
        print("Backend error:", e)
        return jsonify({"answer": "Sorry, I am unable to respond right now."}), 500

if __name__ == "__main__":
    print("🤖 Chatbot server running on http://localhost:5000")
    app.run(port=5000)
