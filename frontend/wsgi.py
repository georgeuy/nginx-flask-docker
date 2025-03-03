
from application import create_app

flask_config = {}

app = create_app(flask_config)

if __name__ == '__main__':
	app.run(debug=True, port=5001)