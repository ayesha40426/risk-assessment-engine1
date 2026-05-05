def analyze_risk(text):
    text = text.lower()

    if "fail" in text or "error" in text or "attack" in text:
        return "HIGH"

    elif "warning" in text or "delay" in text or "slow" in text:
        return "MEDIUM"

    else:
        return "LOW"