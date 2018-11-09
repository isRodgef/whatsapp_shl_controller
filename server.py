import flask
from flask import Flask, request, redirect

app = Flask(__name__)

if __name__ == '__main__':
	app.run(debug=True)