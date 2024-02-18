#!/usr/bin/python3
<<<<<<< HEAD
""" import flask """
from flask import Flask

app = Flask(_name_)


@app.route("/", strict_slashes=False)
def hello():
    """ hello function content """
=======
"""Module to start a Flask web application
That listens on 0.0.0.0, port 5000.
Routes: Then Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


# Define the route for the root
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
>>>>>>> 36e3c944a00b3dc7a2acc53a91d6557ee3a8ae4e
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """hbnb content return"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def addText(text):
    """add variable function starting with 'C' then text"""
    text = text.replace("_", " ")
    return 'C {}'.format(text)


if _name_ == "_main_":
=======
    """Display 'HBNB'"""
    return "HBNB"


if __name__ == "__main__":
>>>>>>> 36e3c944a00b3dc7a2acc53a91d6557ee3a8ae4e
    app.run(host="0.0.0.0", port=5000)
