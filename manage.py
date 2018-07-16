""""Application Entry Point."""

import os

# third-party imports
from flask_script import Manager # controller class for handling commands

# local imports
from app import create_app

# application development instance
app = create_app(config_name=os.getenv("FLASK_CONFIG"))

# initializing the manager object
manager = Manager(app)

@manager.command
def run():
    app.run()


if __name__ == "__main__":
    manager.run()
