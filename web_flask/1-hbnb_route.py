#!/usr/bin/python3
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

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
