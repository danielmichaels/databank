from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from web.config import config

toolbar = DebugToolbarExtension()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    toolbar.init_app(app)

    with app.app_context():
        from web.core import routes

        app.register_blueprint(routes.core)
        # app.register_blueprint(core)

        return app
