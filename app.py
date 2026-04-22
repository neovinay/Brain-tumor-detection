#!/usr/bin/env python
import os
import sys

from flask import Flask, request, jsonify, send_file, render_template
from io import BytesIO
from PIL import Image, ImageOps
import base64
import urllib

import numpy as np
# import scipy.misc - deprecated and unused
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import tensorflow as tf
from tensorflow import keras


# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
# from gevent.pywsgi import WSGIServer - unused
from tensorflow.keras.models import load_model



app = Flask(__name__)
 

# Load your trained model
model = load_model('save.h5')
print("Model loaded successfully")
 


@app.route("/")
@app.route("/first")
def first():
	return render_template('first.html')
    
@app.route("/login")
def login():
	return render_template('login.html')    
@app.route("/chart")
def chart():
	return render_template('chart.html')

@app.route("/performance")
def performance():
	return render_template('performance.html')

users = {} # Memory storage: username: password

@app.route("/signup")
def signup():
	return render_template('signup.html')

@app.route("/register", methods=['POST'])
def register():
	uname = request.form['uname']
	pwd = request.form['pwd']
	if uname in users:
		return render_template('signup.html', error="User exists!")
	users[uname] = pwd
	return redirect(url_for('index'))

@app.route("/login_verify", methods=['POST'])
def login_verify():
	uname = request.form['uname']
	pwd = request.form['pwd']
	if uname in users and users[uname] == pwd:
		return redirect(url_for('index'))
	return render_template('login.html', error="Invalid credentials!")


@app.route("/index",methods=['GET'])
def index():
	return render_template('index.html')


@app.route("/upload", methods=['POST'])
def upload_file():
	print("Hello")
	try:
		img = Image.open(BytesIO(request.files['imagefile'].read())).convert('RGB')
		img = ImageOps.fit(img, (224, 224), Image.Resampling.LANCZOS)
		print("Image processed OK")
	except:
		print("Image load error")
		error_msg = "Please choose an image file!"
		return render_template('index.html', **locals())

	print("About to predict")

# Call Function to predict
args = {'input' : img}
try:
	out_pred, out_prob = predict(args)
	print("Predict success:", out_pred, out_prob)
except Exception as e:
	print("Predict error:", str(e))
	error_msg = "Prediction failed: " + str(e)
	return render_template('index.html', **locals())
out_prob = out_prob * 100

	print("Rendering result with:", out_pred, out_prob)

	print(out_pred, out_prob)
	danger = "danger"
	if out_pred=="You Are Safe, But Do keep precaution":
		danger = "success"
	print(danger)
	img_io = BytesIO()
	img.save(img_io, 'PNG')

	png_output = base64.b64encode(img_io.getvalue())
	processed_file = urllib.parse.quote(png_output)

	return render_template('result.html',**locals())
def predict(args):
	img = np.array(args['input']) / 255.0
	img = np.expand_dims(img, axis = 0)

	global model
	print("Using global model")

	pred = model.predict(img)

	if np.argmax(pred, axis=1)[0] == 0:
		out_pred = "Result: Brain Tumor  Symptoms: unexplained weight loss, double vision or a loss of vision, increased pressure felt in the back of the head, dizziness and a loss of balance, sudden inability to speak, hearing loss, weakness or numbness that gradually worsens on one side of the body."
	elif np.argmax(pred, axis=1)[0] ==1:
		out_pred = "You Are Safe, But Do keep precaution"

	return out_pred, float(np.max(pred))
 
 

if __name__ == '__main__':
    app.run(debug=True)

