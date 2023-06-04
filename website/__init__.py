from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__) # Create a Flask application instance
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQL_ALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .views import views # (Relative) import inside the python package
    from .auth import auth
    
    app.register_blueprint(views, url_prefix="/") # Register the views Blueprint with the application
    app.register_blueprint(auth, url_prefix="/")
    
    from .models import User
    
    create_database(app)
    
    return app # Return the created application instance

def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created database!")