#!/usr/bin/python3
"""
Start a flask app
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Print hello HBNB
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Print HBNB
    """
    return 'HBNB'


@app.route('/c//<text>', strict_slashes=False)
def cisfun(text):
    """
    Print Cfollowed by value of the text
    """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
