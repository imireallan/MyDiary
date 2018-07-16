# config.py

import os

class Config(object):
    """Default Settings."""
    DEBUG = False
    TESTING = False
    SECRET = os.getenv('SECRET')
    RESTPLUS_VALIDATE = True

class DevelopmentConfig(Config):
    """Development Settings."""
    DEBUG = True

class TestingConfig(Config):
    """Testing Settings."""
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Settings."""
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
