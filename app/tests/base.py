from flask_testing import TestCase
from app.apis.models.entries import Entry
from manage import app


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('app.apis.config.TestingConfig')
        return app

    def setUp(self):
        self.entry = Entry()
        self.data = self.entry.create_entry({"title":"test1", "contents":"contents1"})
    
    def tearDown(self):
        self.entry.no_of_entries.clear()
