from flask import Flask, request
from flask_restplus import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from config import app_config


db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    return app
# Create bucket list

# Retrieve item

# Update it

# Delete it