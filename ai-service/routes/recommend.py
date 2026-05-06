from flask import Blueprint, request, jsonify
from services.recommend_service import build_prompt
from services.ai_engine import analyze_risk

recommend_bp = Blueprint("recommend", __name__)

@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    try:
        data = request.get_json()

        # ✅ Input validation
        if not data or "text" not in data:
            return jsonify({"error": "Missing 'text' field"}), 400

        text = data["text"]

        # ✅ Day 15: Empty input validation
        if not text.strip():
            return jsonify({"error": "Input text cannot be empty"}), 400

        # Build prompt
        prompt = build_prompt(text)

        # AI logic
        risk = analyze_risk(text)

        return jsonify({
            "status": "success",
            "input": text,
            "risk_level": risk,
            "prompt": prompt,
            "message": "Analysis completed successfully"
        }), 200

    except Exception as e:
        return jsonify({
            "error": "Internal server error",
            "details": str(e)
        }), 500