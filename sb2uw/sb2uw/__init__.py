# -*- coding: utf-8 -*-

"""
This file contains the application factory, and it tells Python that the sb2uw
directory should be treated as a package.
"""
import os

from flask import (
    Flask,
    Response,
    current_app,
    g,
    jsonify,
    request,
)

from sb2uw.views import home
from sb2uw.views import auth

from werkzeug.exceptions import HTTPException
# login failed handler, from:
# https://computableverse.com/blog/flask-admin-using-basicauth
# 登录失败控制器，来源：
# https://computableverse.com/blog/flask-admin-using-basicauth
class AuthException(HTTPException):
    def __init__(self, message):
        # python 2
        # super(AuthException, self).__init__(message, Response(
        #     message, 401,
        #     {'WWW-Authenticate': 'Basic realm="Login Required"'}
        # ))
        # # python 3
        super().__init__(message, Response(
            message, 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))

def create_app(test_config=None):
    """Construct the core application."""

    # Load our configs
    app = Flask(__name__, instance_relative_config=True)

    # dynamically change configuration
    if os.environ.get('FLASK_ENV') == 'production':
        app.config.from_object('config.ProductionConfiguration')

        dashboard.config.init_from(file='instance/flask_monitoring_dashboard_config.cfg')
        dashboard.bind(app)

    elif os.environ.get('FLASK_ENV') == 'staging':
        app.config.from_object('config.StagingConfiguration')

        dashboard.config.init_from(file='instance/flask_monitoring_dashboard_config.cfg')
        dashboard.bind(app)

    else:
        app.config.from_object('config.DevelopmentConfiguration')

    app.config.from_pyfile('config.py')  # instance

    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'youremail@address.com'
    app.config['MAIL_PASSWORD'] = 'emailpassword'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    app.config["UPLOAD_FOLDER"] = "uploads/media" # join(dirname(realpath(__file__)), "uploads/media")
    app.config["ALLOWED_EXTENSIONS"] = ["jpg", "png", "mov", "mp4", "mpg"]
    app.config["MAX_CONTENT_LENGTH"] = 1000 * 1024 * 1024  # 1000mb

    # Register Blueprints
    app.register_blueprint(home.bp)
    app.register_blueprint(auth.bp)

    # Error handlers
    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify("{}".format(error)), 404

    @app.errorhandler(400)
    def page_not_found(error):
        return jsonify("{}".format(error)), 400

    @app.errorhandler(500)
    def page_not_found(error):
        return jsonify("{}".format(error)), 500

    return app
