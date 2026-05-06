def get_risk_score(level):
    mapping = {
        "Low": 30,
        "Medium": 60,
        "High": 90
    }
    return mapping.get(level, 0)