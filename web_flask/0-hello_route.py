#!/usr/bin/python3
<<<<<<< HEAD
""" import flask """
from flask import Flask

app = Flask(_name_)


@app.route("/", strict_slashes=False)
def hello():
    """ app content """
    return "Hello HBNB!"


if _name_ == "_main_":
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
    return "Hello HBNB!"


if __name__ == "__main__":
>>>>>>> 36e3c944a00b3dc7a2acc53a91d6557ee3a8ae4e
    app.run(host="0.0.0.0", port=5000)
