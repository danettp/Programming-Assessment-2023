from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


def create_app():
    app = Flask(__name__) # Create a Flask application instance
    app.config['SECRET_KEY'] = "helloworld"
    
    return app # Return the created application instance
