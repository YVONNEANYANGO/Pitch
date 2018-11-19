from flask import Flask, redirect, render_template
from .config import DevConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

# from app import views
# from app import error


# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)

# Initializing Flask Extensions
bootstrap = Bootstrap(app)
db = SQLAlchemy()

from app import views