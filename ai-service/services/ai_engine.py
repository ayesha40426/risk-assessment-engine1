def analyze_risk(text):
    text = text.lower()

    # High-risk keywords
    high_keywords = [
        "fail",
        "failed",
        "error",
        "attack",
        "unauthorized",
        "breach",
        "malware",
        "hacking",
        "multiple login",
        "data leak",
        "critical"
    ]

    # Medium-risk keywords
    medium_keywords = [
        "warning",
        "delay",
        "slow",
        "suspicious",
        "unknown",
        "midnight",
        "unusual",
        "high traffic",
        "latency"
    ]

    # Check for HIGH risk
    for word in high_keywords:
        if word in text:
            return "HIGH"

    # Check for MEDIUM risk
    for word in medium_keywords:
        if word in text:
            return "MEDIUM"

    # Default LOW risk
    return "LOW"