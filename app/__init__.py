from flask import Flask, redirect, render_template
# from .config import DevConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from .config import config_options
from flask_login import LoginManager
from . import *
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
# from app import views
# from app import error


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# from app import views
# return app
db = SQLAlchemy()
bootstrap = Bootstrap()

photos = UploadSet('photos',IMAGES)

mail = Mail()

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Configure UploadSet
    configure_uploads(app,photos)

    # Initializing flask extensions
    bootstrap.init_app(app)
    mail.init_app(app)

    # db = SQLAlchemy()
    db.init_app(app)
    login_manager.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    return app
