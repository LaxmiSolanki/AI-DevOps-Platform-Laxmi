import os

from dotenv import load_dotenv
from flask import Flask, jsonify


load_dotenv()

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "development")
APP_PORT = int(os.getenv("APP_PORT", "5000"))


@app.route("/")
def home():
    return "AI DevOps Platform is running"


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "environment": APP_ENV
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT)