#!/usr/bin/python3
"""import flask"""
from flask import Flask, render_template
from models import storage

app = Flask(_name_)


@app.route("/states", strict_slashes=False)
def fetchStates():
    """ displays html of all states"""
    states = storage.all("State")
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def fetchStateById(id):
    """fetch state by id, if it exits"""
    for states in storage.all("State").values():
        if states.id == id:
            return render_template("9-states.html", states=states)
    return render_template('9-states.html')


@app.teardown_appcontext
def removeSession(exception):
    """ teardown current sql session"""
    storage.close()


if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
