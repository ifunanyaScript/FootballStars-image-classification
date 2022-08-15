from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

@app.route("/classify_image", methods=["GET", "POST"])
def classify_image():
    image = request.form["image_data"]

    response = jsonify(utils.classify_image(image))

    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server for Football Stars Classification.")
    utils.load_aritifacts()
    app.run(port=5000)