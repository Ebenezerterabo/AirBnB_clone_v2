#!/usr/bin/python3
""" Starts a Flash Web Application """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def diplay():
    """ Return Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Return HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """ Display C followed by the value of the text variable """
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
