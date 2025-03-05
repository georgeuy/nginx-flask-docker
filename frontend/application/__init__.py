from flask import Flask
import socket

def create_app(flask_config):

    app = Flask(__name__)

    app.config.from_object(flask_config)

    with app.app_context():

        app.get('/')
        def home():
            return f"Welcome from flask app! #{socket.gethostname()}"

        app.get('/api/v1/healt/<micro>')
        def test_api(micro):
            data = {}
            try:
                if micro == '1':
                    # Consumir datos desde micro-1
                    response = requests.get("http://micro-1:3000/")
                    data = response.json()
                elif micro == '2':
                    # Consumir datos desde micro-2
                    response = requests.get("http://micro-2:3000/")
                    data = response.json()
                else:
                    data = {'error':'micro does not exists'}
                return jsonify(data)
            except requests.exceptions.RequestException as e:
                data = {'error': f'No se pudo conectar al micro-{micro}', 'details': str(e)}

        ########################## BLUEPRINTS ##########################

        from .views.stock import stock_bp
        app.register_blueprint(stock_bp)


        ##########################    ERRORS   ##########################


        return app
