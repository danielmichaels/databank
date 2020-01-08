import os


class BaseConfig:
    AUTO_LOAD_TEMPLATES = True
    DEBUG = False
    TESTING = False
    SESSION_KEY = os.environ.get("SECRET_KEY") or '1243243424'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,

    "default": DevelopmentConfig,
}
