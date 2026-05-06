def format_response(data):
    return {
        "risk": data.get("risk_level"),
        "score": data.get("risk_score"),
        "category": data.get("category"),
        "confidence": data.get("confidence"),
        "reason": data.get("reason"),
        "impact": data.get("impact"),
        "recommendations": data.get("recommendations")
    }