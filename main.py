from flask import Flask, render_template, request, jsonify
from modules.helpers.connector import Connector
from modules.core.scraper import ScraperV3

app = Flask(__name__, template_folder="public", static_folder="public")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/hardcode", methods=["POST"])
def check_hardcode_article():
    data = request.get_json()
    title = data["title"]
    article = data["article"]
    prediction, scores = Connector(title, article).execute() 
    return jsonify({
        "success": True,
        "prediction": prediction,
        "scores": scores
    })

@app.route("/url", methods=["POST"])
def check_url_article():
    data = request.get_json()
    url = data["url"]
    prediction, scores = Connector("","",url).execute() 
    return jsonify({
        "success": True,
        "prediction": prediction,
        "scores": scores
    })

if __name__ == "__main__":
    app.run(debug=True)