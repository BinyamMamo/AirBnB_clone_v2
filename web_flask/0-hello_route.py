#!/usr/bin/python3
"""Uses flask to display text"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """return the string "Hello, HBNB!".
    """
    return 'Hello HBNB!'


app.run(host='0.0.0.0', port=5000)
