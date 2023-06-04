from flask import Blueprint, render_template, redirect, url_for

auth = Blueprint("auth", __name__) # Create a Blueprint instance named "auth"

@auth.route("/login") # Define a route for the "/login" URL
def login():
    return render_template("login.html") # Render "login.html" template and return it as the response

@auth.route("/sign-up") 
def sign_up():
    return render_template("signup.html")

@auth.route("/logout") 
def logout():
    return redirect(url_for("views.home"))