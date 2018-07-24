from flask_testing import TestCase
from manage import app

from app.apis.models.model import User


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('app.apis.config.TestingConfig')
        return app

    def setUp(self):
        self.user = User(
            id=1,
            username="imireallan",
            email='imireallan@gmail.com',
            password='password',
            confirm='password'
        )
        self.entry = {
            "title": "first title",
            "contents": "first content"
        }

    def tearDown(self):
        pass