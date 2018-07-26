import unittest

# third-party imports
from flask_testing import TestCase

from manage import app


class TestDevelopmentSettings(TestCase):
    def create_app(self):
        app.config.from_object('app.apis.config.DevelopmentConfig')
        return app

    def test_development_config(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'thisisit')
        self.assertFalse(app.config['DEBUG'] is False)



class TestTestingSettings(TestCase):
    def create_app(self):
        app.config.from_object('app.apis.config.TestingConfig')
        return app

    def test_testing_config(self):
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])


class TestProductionSettings(TestCase):
    def create_app(self):
        app.config.from_object('app.apis.config.ProductionConfig')
        return app

    def test_production_configs(self):
        self.assertTrue(app.config['TESTING'] is False)


if __name__ == '__main__':
    unittest.main()