#!/usr/bin/python3
"""Start web application with two routings
"""

from flask import Flask
app = Flask(_name_)


@app.route('/')
def hello():
    """Return string when route queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return string when route queried
    """
    return 'HBNB'

if _name_ == '_main_':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
