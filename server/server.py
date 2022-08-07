from crypt import methods
from flask import Flask, request, jsonify
# import utils

app = Flask(__name__)

@app.route("/classsify_image", methods=["GET", "POST"])
def classify_image():
    return "hi"

if __name__ == "__main__":
    app.run(port=5000)