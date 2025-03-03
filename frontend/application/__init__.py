from flask import Flask
import socket

def create_app(flask_config={}):

	app = Flask(__name__)

	@app.route('/')
	def home():

		return f"Welcome from flask app! #{socket.gethostname()}"

	return app
