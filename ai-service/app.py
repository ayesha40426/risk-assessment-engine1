from flask import Flask
from routes.recommend import recommend_bp

app = Flask(__name__)

# Register blueprint
app.register_blueprint(recommend_bp)

@app.route("/")
def home():
    return {"message": "AI Service is running"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)