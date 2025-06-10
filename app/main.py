from flask import Flask, jsonify
from apis.catfacts import get_cat_fact
from apis.postman_echo import get_echo

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API Automation QA Tool"})

@app.route("/echo")
def echo():
    return jsonify(get_echo().json())

@app.route("/catfact")
def catfact():
    return jsonify(get_cat_fact().json())

if __name__ == "__main__":
    app.run(debug=True)
