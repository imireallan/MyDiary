import unittest
import os

# third-party imports
from flask_testing import TestCase

# local imports
from manage import app

class TestDevelopmentConfig(TestCase):
    """TestCase for the development config."""

    def create_app(self):
        app.config.from_object('app.apis.config.DevelopmentConfig')
        return app

    def test_development_configs(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(app.config['SECRET_KEY'] is "thisismysecretkey")

class TestTestingConfig(TestCase):
    """TestCase for the testing config."""

    def create_app(self):
        app.config.from_object('app.apis.config.TestingConfig')
        return app

    def test_testing_configs(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['TESTING'] is True)

class TestProductionConfig(TestCase):
    """TestCase for the development config."""

    def create_app(self):
        app.config.from_object('app.apis.config.ProductionConfig')
        return app

    def test_production_configs(self):
        self.assertFalse(app.config['DEBUG'] is True)
        self.assertFalse(app.config['TESTING'] is True)



if __name__ == "__main__":
    unittest.main()