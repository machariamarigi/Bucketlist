""" this module deals with the creation of the application"""

from flask import Flask, render_template
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

    from .profile import profile as profile_blueprint
    app.register_blueprint(profile_blueprint)

    from .bucketlist import bucketlist as bucketlist_blueprint
    app.register_blueprint(bucketlist_blueprint)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('500.html', title='Server error'), 500

    return app
