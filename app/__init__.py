from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from app import views
from app import error

#Initializing application
app = Flask(__name__,instance_relative_config=True,)

#Setting up configurationa
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing Flask Extensions
Bootstrap = Bootstrap(app)

from app import views