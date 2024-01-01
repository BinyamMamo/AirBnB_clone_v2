#!/usr/bin/python3

from flask import Flask, abort

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
	return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
	return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def displayC(text):
	return "C {}".format(text.replace('_', ' '))

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def displayPython(text="is cool"):
	return "Python {}".format(text.replace("_", " "))

@app.route("/number/<n>", strict_slashes=False)
def isNumber(n):
	if n.isdigit():
		return "{} is a number".format(n)
	abort(404)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)