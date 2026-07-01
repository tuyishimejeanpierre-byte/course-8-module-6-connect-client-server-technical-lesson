from flask import Flask, jsonify, send_from_directory
from store import get_sample_data

app = Flask(__name__, static_folder='../client', static_url_path='')

@app.route("/", methods=["GET"])
def welcome():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify(get_sample_data()), 200

if __name__ == "__main__":
    app.run(debug=True)