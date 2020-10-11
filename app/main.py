from flask import Flask, request
from utils import ()

app = Flask(__name__)

@app.route("/predict_genre", methods = ['POST'])
def predict_genre():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')