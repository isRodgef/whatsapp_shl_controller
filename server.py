import flask
from flask import Flask, request, redirect

app = Flask(__name__)



@app.route("/whatsapp",methods=['GET', 'POST'])
def reply():
    return ";"

if __name__ == '__main__':
	app.run(debug=True)