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


@app.route('/states_list', strict_slashes=False)
def display_states():
    """
    display all states in HTML page
    """
    return render_template('7-states_list.html',
                           states=storage.all("State").values())


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
