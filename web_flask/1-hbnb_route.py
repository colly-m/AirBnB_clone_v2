#!/usr/bin/python3
""" import flask """
from flask import Flask

app = Flask(_name_)


@app.route("/", strict_slashes=False)
def hello():
    """ hello function content """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnh content"""
    return "HBNB"


if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
