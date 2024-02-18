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
    """hbnb content return"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def addText(text):
    """add variable function starting with 'C' then text"""
    text = text.replace("_", " ")
    return 'C {}'.format(text)


if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
