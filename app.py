# third-party imports
from flask import Flask

# local imports
from config import app_config
from apis import api

def create_app(config_name):
    """Enables having instances of the
    application with different settings
    """

    # initializing the app
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    api.init_app(app)

    return app