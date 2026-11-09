import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({"fixture": "python", "status": "ok"})

@app.get("/__shiplet/health")
def health():
    return ("", 204)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8000")))
