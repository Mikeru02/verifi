from flask import Flask, render_template, request, jsonify
from modules.helpers.connector import Connector
from modules.core.converter import Converter
from PIL import Image
import pytesseract

app = Flask(__name__, template_folder="public", static_folder="public")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/hardcode", methods=["POST"])
def check_hardcode_article():
    data = request.get_json()
    title = data["title"]
    article = data["article"]
    prediction, scores, confidence = Connector(title, article).execute() 
    return jsonify({
        "success": True,
        "prediction": prediction,
        "scores": scores,
        "confidence": confidence
    })

@app.route("/url", methods=["POST"])
def check_url_article():
    data = request.get_json()
    url = data["url"]
    prediction, scores, confidence = Connector("","",url).execute() 
    return jsonify({
        "success": True,
        "prediction": prediction,
        "scores": scores,
        "confidence": confidence
    })

@app.route("/image", methods=["POST"])
def check_image():
    data = request.get_json()
    image = data["file_name"]
    full_url = f"data/pictures/{image}"
    converter = Converter("image", full_url).execute()
    prediction, scores, confidence = Connector("", converter).execute() 

    return jsonify({
        "success": True,
        "prediction": prediction,
        "scores": scores,
        "confidence": confidence
    })
if __name__ == "__main__":
    app.run(debug=True)