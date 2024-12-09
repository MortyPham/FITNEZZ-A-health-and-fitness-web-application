import requests

from flask import redirect, render_template, session
from functools import wraps

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function

def get_status(height, weight):
    height = float(height)
    weight = float(weight)

    BMI = weight / (height/100)**2

    print(height)

    if BMI <= 18.4:
        return ("underweight.")
    elif BMI <= 24.9:
        return ("healthy.")
    elif BMI <= 29.9:
        return ("overweight.")
    elif BMI <= 34.9:
        return ("severely overweight.")
    elif BMI <= 39.9:
        return ("obese.")
    else:
        return ("severely obese.")
