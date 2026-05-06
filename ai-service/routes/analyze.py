from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from services.scoring_service import get_risk_score
from utils.formatter import format_response
import json
from datetime import datetime

analyze_bp = Blueprint("analyze", __name__)

def clean(text):
    return text.replace("```json", "").replace("```", "").strip()

def load_prompt(text):
    with open("prompts/analyze_prompt.txt") as f:
        return f.read().replace("{input}", text)

@analyze_bp.route("/analyze", methods=["POST"])
def analyze():
    # ✅ Input validation
    if not request.json or "text" not in request.json:
        return jsonify({
            "error": "Invalid input. 'text' field is required"
        }), 400

    text = request.json.get("text")

    # ✅ Empty input check
    if not text.strip():
        return jsonify({
            "error": "Input text cannot be empty"
        }), 400

    try:
        prompt = load_prompt(text)
        result = call_groq(prompt)

        # ✅ Parse AI response
        try:
            parsed = json.loads(clean(result))
        except Exception:
            return jsonify({
                "error": "AI response parsing failed",
                "raw": result
            }), 500

        # ✅ Day 12: Add risk score
        parsed["risk_score"] = get_risk_score(parsed.get("risk_level"))

        # ✅ Day 13: Format response
        formatted = format_response(parsed)

        return jsonify({
            "status": "success",
            "data": formatted,
            "generated_at": str(datetime.now())
        })

    except Exception as e:
        return jsonify({
            "error": "Internal server error",
            "details": str(e)
        }), 500