#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello():
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


@app.route('/python/', strict_slashes=False)
def display_is_cool(text="is cool"):
    """ Displays 'Python is cool' """
    return "Python " + text


@app.route('/python/<text>', strict_slashes=False)
def display_python(text="is cool"):
    """ Displays 'Python' followed by the value of the text variable """
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ Displays 'n is a number only if n is an integer' """
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
