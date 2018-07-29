import json
from flask_testing import TestCase
from manage import app
from app.database import Database

from app.apis.models.model import User, Entry


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('app.apis.config.TestingConfig')
        return app

    def setUp(self):
        self.db = Database()
        self.cursor = self.db.cursor
        self.dict_cursor = self.db.dict_cursor
        self.db.drop_all()
        self.db.create_tables()
        
        self.user = User(
            id=1,
            username="imireallan",
            email='imireallan@gmail.com',
            password='password',
            confirm='password'
        )
        self.entry_obj = Entry(
            id=1,
            title="first entry model test",
            contents='testing is very essential',
            user_id="1"
        )
        self.entry = json.dumps(
            {
                "title": "first test",
                "contents": "tdd is awesome"
            }
        )
        self.entry_no_title = json.dumps(
            {
                "title": "",
                "contents": "tdd is awesome"
            }
        )
        self.entry_no_contents = json.dumps(
            {
                "title": "first test",
                "contents": ""
            }
        )
        self.update_entry = json.dumps(
            {
                "title": "first edition",
                "contents": "tdd is very awesome"
            }
        )

    def tearDown(self):
        self.db.drop_all()