from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
import json

recommend_bp = Blueprint("recommend", __name__)

def load_prompt(text):
    with open("ai-service/prompts/recommend_prompt.txt") as f:
        return f.read().replace("{input}", text)

def clean_response(text):
    # Remove markdown formatting
    text = text.replace("```json", "").replace("```", "").strip()
    return text

@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    text = data.get("text")

    if not text:
        return jsonify({"error": "No input provided"}), 400

    prompt = load_prompt(text)
    result = call_groq(prompt)

    cleaned = clean_response(result)

    try:
        parsed = json.loads(cleaned)
    except:
        parsed = {"raw": cleaned}

    return jsonify({
        "recommendations": parsed
    })