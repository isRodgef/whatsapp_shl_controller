import flask
from flask import Flask, request, redirect
from twilio.rest import Client
from credentials import * 

app = Flask(__name__)



@app.route("/whatsapp",methods=['GET', 'POST'])
def reply():
    client = Client(account_sid,auth_token)
    message = client.messages.create(body= "hello",from_=sender,to=receiver)
    return ";"

if __name__ == '__main__':
	app.run(debug=True)