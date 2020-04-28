from flask import Flask
from .config import DevConfig,Config
from flask_bootstrap import Bootstrap
# from instance.config import MOVIE_API_KEY

#Initializing application
app = Flask(__name__,instance_relative_config=True,)

#Setting up configuration
app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

# Getting api key
app.config['MOVIE_API_KEY'] = Config.MOVIE_API_KEY

# Getting the movie base url
app.config["MOVIE_API_BASE_URL"] =  Config.MOVIE_API_BASE_URL

# Initializing Flask Extensions
Bootstrap = Bootstrap(app)

from app import views
from app import error