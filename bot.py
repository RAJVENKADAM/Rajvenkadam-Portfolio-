# bot.py
import os
from groq import Groq

# Initialize Groq client
client = Groq(api_key=os.environ.get('GROQ_API_KEY'))  # Load from environment variable

# Load your personal info from data.txt
with open("data.txt", "r", encoding="utf-8") as f:
    personal_info = f.read()

def ask_bot(question):
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

Answer questions **only if they are about Rajvenkadam S**.
Keep your answers **short, sweet, confident, and friendly**.
If the question is about his skills, respond **strongly and affirmatively**.
If the question is unrelated, respond politely:
"I only answer questions about Rajvenkadam S."
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
