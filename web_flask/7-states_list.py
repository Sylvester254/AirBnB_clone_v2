#!/usr/bin/python3
"""
Start a flask app
"""
from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.teardown_appcontext
def rm_curr_SQLAlchemy(exception):
    """
    Remove the current SQLAlchemy Session after each request 
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states():
    """
    display all states in HTML page
    """
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
