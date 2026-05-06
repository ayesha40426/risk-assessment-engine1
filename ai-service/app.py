from flask import Flask
from flask_cors import CORS

# Import all route blueprints
from routes.describe import describe_bp
from routes.recommend import recommend_bp
from routes.categorise import categorise_bp
from routes.analyze import analyze_bp   # Day 11

app = Flask(__name__)
CORS(app)

# ✅ Register all routes
app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)
app.register_blueprint(categorise_bp)
app.register_blueprint(analyze_bp)

# ✅ Home route
@app.route("/")
def home():
    return {
        "message": "Risk Assessment Engine AI Service is running"
    }

# ✅ Health check (important for testing)
@app.route("/health")
def health():
    return {
        "status": "ok"
    }

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)