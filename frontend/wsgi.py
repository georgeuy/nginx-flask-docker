import os
from application import create_app

from dotenv import load_dotenv

load_dotenv('.env', verbose=True)

flask_config = os.environ['FLASK_CONFIG']

app = create_app(flask_config)

if __name__ == '__main__':
	app.run(debug=True, port=5000)