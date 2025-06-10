import sys
import os
from flask import Flask, jsonify

# Add project root to sys.path so Python can find the 'apis' package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from apis.catfacts import get_cat_fact
from apis.postman_echo import get_echo

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API Automation QA Tool"})

@app.route("/catfact")
def catfact():
    return jsonify(get_cat_fact().json())

@app.route("/echo")
def echo():
    return jsonify(get_echo().json())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # default to 5000 if not set
    app.run(host="0.0.0.0", port=port, debug=True)
