""" this module deals with the creation of the application"""

from flask import Flask
from flask_bootstrap import Bootstrap

from config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    Bootstrap(app)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .profile import profile as profile_blueprint#
    app.register_blueprint(profile_blueprint)

    return app
