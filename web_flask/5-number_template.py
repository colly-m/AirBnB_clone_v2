#!/usr/bin/python3
<<<<<<< HEAD
"""Module to start a Flask web application
That listens on 0.0.0.0, port 5000.
Routes: Then Displays 'Hello HBNB!', 'HBNB', 'C', and 'Python'
"""
from flask import Flask

app = Flask(__name__)


# Define the route for the root
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
=======
""" import flask """
from flask import Flask, render_template

app = Flask(_name_)


@app.route("/", strict_slashes=False)
def hello():
    """ hello function content """
>>>>>>> 86da52e0e9c4ee51b1598d7e836a4ed81bee12e3
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """Display 'HBNB'"""
=======
    """hbnb content return"""
>>>>>>> 86da52e0e9c4ee51b1598d7e836a4ed81bee12e3
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
<<<<<<< HEAD
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
    """Displays an HTML page only if <n> is an integer."""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
=======
def addText(text):
    """add variable function starting with 'C' then text"""
    text = text.replace("_", " ")
    return 'C {}'.format(text)


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text):
    """ display 'python' followed by the value 'text'"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def checkIfNum(n):
    """check if n is a number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def displayHtml(n):
    """render template only if n is a number"""
    return render_template('5-number.html', n=n)


if _name_ == "_main_":
>>>>>>> 86da52e0e9c4ee51b1598d7e836a4ed81bee12e3
    app.run(host="0.0.0.0", port=5000)
