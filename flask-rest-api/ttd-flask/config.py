import os
basedir = os.path.abspath(os.path.dirname(__file__))
db_name = 'todo.db'

class Config:
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = "thisisjustadummyaccount-idodosecurityirl"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, db_name)

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, f"test_{db_name}")
    DEBUG = True

class StagingConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


app_config = {
    'developement': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}