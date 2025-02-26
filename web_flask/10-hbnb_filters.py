#!/usr/bin/python3
"""
Start a flask app
"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.teardown_appcontext
def rm_curr_SQLAlchemy(error):
    """
    Remove the current SQLAlchemy Session after each request 
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def display_states():
    """
    display all states in HTML page
    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
