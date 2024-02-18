#!/usr/bin/python3
"""Module to start a Flask web application
That listens on 0.0.0.0, port 5000.
Routes: Then Displays 'Hello HBNB!', 'HBNB', 'C', and 'Python'
        '<n> is a number if only <n> is an integer'
        'Displays value of <n>
        'AN HTML page only if <n> is an int' also stating if
        <n> is even or odd'
"""
from flask import Flask

app = Flask(__name__)


# Define the route for the root
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """Displays C followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """Displays Python followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def isNum(n):
    """Displays “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    """Displays an HTML page only if <n> is an integer.
    Displays the value of <n> in the body.
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def numIsodd_or_even(n):
    """Displays an HTML page only if <n> is an integer.
    States whether <n> is odd or even in the body.
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
