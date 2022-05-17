from flask import Flask, render_template, request
from test_utils import *

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/prediction', methods=["GET", "POST"])
def prediction():
	if request.method == "POST" and "username" in request.form:
		username = request.form['username']
		model_prediction, tweets = get_prediction(username)
		return render_template('prediction.html', username=username, predicted_type=model_prediction, tweets=tweets)

app.run(debug=True)
