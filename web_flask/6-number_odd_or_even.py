#!/usr/bin/python3
"""Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False, methods=['GET'])
def hello():
    """Return Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False, methods=['GET'])
def hbnb():
    """Return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False, methods=['GET'])
def CFun(text):
    """Return text"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False, methods=['GET'])
@app.route('/python/', strict_slashes=False, methods=['GET'])
@app.route('/python/<text>', strict_slashes=False, methods=['GET'])
def python_url(text="is cool"):
    """Return text"""
    if text is None:
        return "Python {}".format(text)
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False, methods=['GET'])
def number(n):
    """Return n is a number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False, methods=['GET'])
def number_template(n):
    """Return n is a number"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False,
           methods=['GET'])
def number_odd_or_even(n):
    """Return n is a number"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
