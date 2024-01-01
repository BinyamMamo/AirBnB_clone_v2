#!/usr/bin/python3

from flask import Flask, abort, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
	return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
	return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def displayC(text):
	return "C {}".format(text.replace("_", " "))

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def displayPython(text="is cool"):
	return "Python {}".format(text.replace("_", " "))

@app.route("/number/<n>", strict_slashes=False)
def displayNumber(n):
	if n.isdigit():
		return "{} is a number".format(n)
	abort(404)

@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
	if n.isdigit():
		return render_template("5-number.html", number=n)
	abort(404)

@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def odd_or_even(n):
	if n.isdigit():
		e = "odd" if int(n) % 2 else "even"
		return render_template("6-number_odd_or_even.html", num=n, evenity=e)
	abort(404)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)
