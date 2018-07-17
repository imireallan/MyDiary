""""Application Entry Point."""

import os

# third-party imports
from flask_script import Manager # controller class for handling commands

# local imports
from app.apis import create_app

from app import blueprint

# application development instance
app = create_app(config_name=os.getenv("FLASK_CONFIG"))

# registering the blueprint
app.register_blueprint(blueprint)

# initializing the manager object
manager = Manager(app)

@manager.command
def run():
    app.run()


if __name__ == "__main__":
    manager.run()
