from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
import json
from datetime import datetime

categorise_bp = Blueprint("categorise", __name__)

def clean(text):
    return text.replace("```json", "").replace("```", "").strip()

def load_prompt(text):
    with open("prompts/categorise_prompt.txt") as f:
        return f.read().replace("{input}", text)

@categorise_bp.route("/categorise", methods=["POST"])
def categorise():
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

        # ✅ Parse AI response
        try:
            parsed = json.loads(clean(result))
            try:
              parsed["confidence"] = float(parsed.get("confidence", 0))
            except:
                parsed["confidence"] = 0.0 
        
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