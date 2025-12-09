# bot.py
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv(dotenv_path="E:/My App/My Portfolio/.env")

# Get API key from environment
api_key = os.getenv("GROQKEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file!")

# Initialize Groq client
client = Groq(api_key=api_key)

# Load your personal info from data.txt
with open("data.txt", "r", encoding="utf-8") as f:
    personal_info = f.read()

def ask_bot(question: str) -> str:
    """
    Sends the question to the AI model with personal context.
    Only answers if the question is about Rajvenkadam S.
    Responses are short, confident, and friendly.
    """
    try:
        messages = [
            {
                "role": "system",
                "content": f"""
You are a personal assistant for Rajvenkadam S.
You know the following about him:

{personal_info}

Answer questions *only if they are about Rajvenkadam*.
Keep your answers short, in plain paragraphs only—no symbols, headings, titles, or subtitles.
Provide short answers by default. Only give complete paragraphs with detailed explanations when the user specifically asks to explain something.
Avoid sharing any secrets or sensitive information.
If the question is about his skills, respond strongly and affirmatively.
If the question is unrelated, respond politely:
"Sorry, I only answer questions about Rajvenkadam."
"""
            },
            {"role": "user", "content": question}
        ]

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )

        answer = response.choices[0].message.content
        return answer

    except Exception as e:
        print("Error in bot.py:", e)
        return "Sorry, I am unable to respond right now."
