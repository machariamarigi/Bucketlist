""" this module deals with the creation of the application"""

from flask import Flask

from ..config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
