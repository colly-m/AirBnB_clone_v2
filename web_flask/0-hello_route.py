#!/usr/bin/python3
"""Start a flask web app
"""

from flask import Flask
app = Flask(_name_)


@app.route('/')
def hello_flask():
    """Return string when route queried
    """
    return 'Hello HBNB!'

if _name_ == '_main_':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
