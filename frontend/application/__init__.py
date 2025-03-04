from flask import Flask, jsonify
import requests
import socket

def create_app(flask_config={}):

    app = Flask(__name__)

    @app.route('/')
    def home():

        return f"Welcome from flask app! #{socket.gethostname()}"


    @app.route('/api')
    def test_api():     
        try:
            # Consumir datos desde micro-1
            response = requests.get("http://micro-1:3001/")  
            data = response.json()
        except requests.exceptions.RequestException as e:
            data = {'error': 'No se pudo conectar a micro-1', 'details': str(e)}

        return jsonify(data)


    return app
