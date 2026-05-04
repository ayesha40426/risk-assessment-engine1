from flask import Flask
from flask_cors import CORS

from routes.describe import describe_bp
from routes.recommend import recommend_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(port=5000, debug=True)