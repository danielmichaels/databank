from flask import Flask

from web.config import config
from web.core import core


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    with app.app_context():
        app.register_blueprint(core)

        return app
