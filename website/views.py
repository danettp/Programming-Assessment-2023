from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/") # Define a route decorator for the root URL ("/")
def home():
    return "Home"