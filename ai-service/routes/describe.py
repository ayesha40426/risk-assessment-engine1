from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
import json

describe_bp = Blueprint("describe", __name__)

def load_prompt(text):
    with open("ai-service/prompts/describe_prompt.txt") as f:
        return f.read().replace("{input}", text)

def clean_response(text):
    # Remove markdown formatting if present
    text = text.replace("```json", "").replace("```", "").strip()
    return text

@describe_bp.route("/describe", methods=["POST"])
def describe():
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
        "data": parsed,
        "generated_at": "now"
    })