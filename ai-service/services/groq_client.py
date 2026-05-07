import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.getenv("GROQ_API_KEY")

def call_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "user",
                "content": prompt 
            }
        ],
        "temperature": 0.3
    }

    try:
        res = requests.post(
            url,
            headers=headers,
            json=data
        )

        # Check API response
        if res.status_code != 200:
            print("Groq API Error:", res.text)

            return "Fallback: AI unavailable"

        response_json = res.json()

        return response_json["choices"][0]["message"]["content"]

    except Exception as e:
        print("Groq Error:", e)

        return "Fallback: Error occurred"