from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


def create_app():
    app = Flask(__name__) # Create a Flask application instance
    app.config['SECRET_KEY'] = "helloworld"
    
    from .views import views # (Relative) import inside the python package
    from .auth import auth
    
    app.register_blueprint(views, url_prefix="/") # Register the views Blueprint with the application
    app.register_blueprint(auth, url_prefix="/")
    
    return app # Return the created application instance
