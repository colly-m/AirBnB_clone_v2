#!/usr/bin/python3
"""import flask"""
from flask import Flask, render_template
from models import storage

app = Flask(_name_)


@app.route("/states_list", strict_slashes=False)
def fetchStates():
    """ displays html of all states"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def removeSession(exception):
    """ teardown current sql session"""
    storage.close()


if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
