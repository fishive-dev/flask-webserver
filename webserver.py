from flask import Flask, render_template, jsonify, request
import datetime
import random

app = Flask(__name__)

@app.route("/")
def hello():
    vitals_data = {
        'vital1' : "Yo Momma",
        'vital2' : "so fat",
        'vital3' : "I broke",
        'vital4' : "this diss",
        'vital5' : "into parts"
    }
    return render_template('index.html', **vitals_data)

@app.route("/processPost", methods=["POST"])
def processPost():
    data = request.json()
    return data

@app.route("/processGet", methods=["GET"])
def processGet():
    vitals_data = {
        'vital1' : "Yo Momma",
        'vital2' : "so fat",
        'vital3' : "I broke",
        'vital4' : "this diss",
        'vital5' : "into parts"
    }

    return jsonify(vitals_data)

if __name__ == "__main__":
    app.run(host="192.168.2.141", port=42069, debug=True)
    print(app)