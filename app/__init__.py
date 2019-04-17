from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(__name__,instance_relative_config=True) #instance_relative_config is used to allow us to connect to the instance folder when the app instance is created

#Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views