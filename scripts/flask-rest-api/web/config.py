import os


class BaseConfig:
    AUTO_LOAD_TEMPLATES = True
    DEBUG = False
    TESTING = False
    SESSION_KEY = os.environ.get("SECRET_KEY") or '1243243424'
    DEBUG_TB_ENABLED = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'changeme!'
    DEBUG_TB_ENABLED = True


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
