from flask.cli import FlaskGroup
from src import create_app, db
from flask_cors import CORS

src = create_app()
cli = FlaskGroup(src)
CORS(src)

if __name__ == '__main__':
    src.run()
