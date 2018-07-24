# third-party imports
from flask import Flask

# local imports
from .config import app_config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    @app.route("/")
    def index():
        return "hello world"

    return app


