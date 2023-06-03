from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/") # Define a route decorator for the root URL ("/")
@views.route("/home")
def home():
    return render_template("home.html")