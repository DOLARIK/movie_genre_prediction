from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from plot_summary_genre import (get_genre)

app = Flask(__name__)

CORS(app, supports_credentials=True)

@app.route("/genre", methods = ['POST'])
# @cross_origin(supports_credentials=True)
def genre():
	genres_dict = get_genre(request.get_json(force=True))
	response = jsonify(genres_dict)
	return response
		

@app.route("/predict_genre", methods = ['POST'])
def predict_genre():
	input_dict = {"plot_summary": str(request.form['plot_summary'])}
	genres_dict = get_genre(input_dict)
	return jsonify(genres_dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,)