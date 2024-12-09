import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import get_status, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/bmi", methods=["GET", "POST"])
@login_required
def bmi():
    """Calculate BMI and get body status"""
    if request.method == "POST":
        # If user has already enter weight
        if request.form.get("height") and request.form.get("weight"):

            # Get height and weight
            height = float(request.form.get("height"))
            weight = float(request.form.get("weight"))

            # Calculate BMI, health status and age
            BMI = weight / (height/100)**2
            status = get_status(height, weight)
            age = int(request.form.get("age"))

            # Add data about height and weight table
            db.execute(
                "UPDATE users SET height=?, weight=?, bmi=?, status=?, age=? WHERE id=?",
                height, weight, BMI, status, age, session["user_id"]
            )

            return render_template("bmi_calculated.html", BMI=BMI, status=status)

        else:
            return render_template("bmi.html")

    if request.method == "GET":
        # Get body info from users table
        body_info = db.execute("SELECT height, weight, bmi, status FROM users WHERE id=?", session["user_id"])

        # Check if user has already fill in body index
        if body_info[0]['height'] == None or body_info[0]['weight'] == None:
            return render_template("bmi.html")
        else:
            return render_template("bmi_calculated.html", BMI=body_info[0]['bmi'], status=body_info[0]['status'])


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return render_template("login.html", error="Invalid username or password.")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            flash("Must provide username", "danger")
            return redirect("/register")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Must provide password", "danger")
            return redirect("/register")

        # Ensure confirmation field is filled
        elif not request.form.get("confirmation"):
            flash("Please confirm your password", "danger")
            return redirect("/register")

        # Ensure password matches confirmation
        elif request.form.get("password") != request.form.get("confirmation"):
            flash("Passwords do not match", "danger")
            return redirect("/register")

        # Get username and password
        username = request.form.get("username")
        password = request.form.get("password")

        # Add to the database
        try:
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)",
                username, generate_password_hash(password)
            )
        except ValueError:
            flash("Username already exists", "danger")
            return redirect("/register")

        # After successful registration, redirect to login page
        flash("Registration successful! Please log in.", "success")
        return redirect("/login")

    # User reached route via GET
    else:
        return render_template("register.html")

@app.route("/")
def intro():
    """Introduce to web app"""
    try:
        body_info = db.execute("SELECT age, height, weight, bmi, status FROM users WHERE id=?", session["user_id"])
        if body_info[0]["age"] == None:
            return render_template("bmi.html")
        else:
            return render_template("homescreen.html",
                                age=body_info[0]["age"],
                                height=body_info[0]["height"],
                                weight=body_info[0]["weight"],
                                BMI=body_info[0]['bmi'],
                                status=body_info[0]['status'])

    except :
        return render_template("intro.html")

@app.route("/meal", methods=["GET", "POST"])
def meal():
    """Give out tips and helpful instructions for meal"""
    try:
        # Get body information
        body_info = db.execute("SELECT height, weight, bmi, status, age FROM users WHERE id=?", session["user_id"])
        height = body_info[0]["height"]
        weight = body_info[0]["weight"]
        age = body_info[0]["age"]
        calorie_intake = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
        return render_template("meal.html", calorie_intake=calorie_intake)
    except TypeError:
        return render_template("bmi.html")

@app.route("/fitness", methods=["GET", "POST"])
def fitness():
    """Generate fitness plan"""
    return render_template("fitness.html")
