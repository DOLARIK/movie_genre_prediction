from flask import Flask, request, jsonify
from plot_summary_genre import (get_genre)

app = Flask(__name__)

@app.route("/predict_genre", methods = ['POST'])
def predict_genre():
	genres_dict = get_genre(request.get_json())
	return jsonify(genres_dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,)