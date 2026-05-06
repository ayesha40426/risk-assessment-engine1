from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
import json
from datetime import datetime

describe_bp = Blueprint("describe", __name__)

def clean(text):
    return text.replace("```json", "").replace("```", "").strip()

def load_prompt(text):
    with open("prompts/describe_prompt.txt") as f:
        return f.read().replace("{input}", text)

@describe_bp.route("/describe", methods=["POST"])
def describe():
    # ✅ Input validation
    if not request.json or "text" not in request.json:
        return jsonify({
            "error": "Invalid input. 'text' field is required"
        }), 400

    text = request.json.get("text")

    # ✅ Day 15: Empty input validation
    if not text.strip():
        return jsonify({
            "error": "Input text cannot be empty"
        }), 400

    try:
        prompt = load_prompt(text)
        result = call_groq(prompt)

        try:
            parsed = json.loads(clean(result))
        except Exception:
            return jsonify({
                "error": "AI response parsing failed",
                "raw": result
            }), 500

        return jsonify({
            "status": "success",
            "data": parsed,
            "generated_at": str(datetime.now())
        })

    except Exception as e:
        return jsonify({
            "error": "Internal server error",
            "details": str(e)
        }), 500