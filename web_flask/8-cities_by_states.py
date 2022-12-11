#!/usr/bin/python3
"""
Start a flask app
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def rm_curr_SQLAlchemy(error):
    """
    Remove the current SQLAlchemy Session after each request 
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states():
    """
    display all states in HTML page
    """
    return render_template('7-states_list.html',
                           states=storage.all(State).values())


@app.route('/cities_by_states', strict_slashes=False)
def display_cities():
    """
    display a HTML page of cities by states
    """
    return render_template('8-cities_by_states.html',
                           states=storage.all(State).values())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
