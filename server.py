import flask
from flask import Flask, request, redirect
from twilio.rest import Client
from twilio import twiml
from credentials import * 
from subprocess import Popen, PIPE

app = Flask(__name__)



@app.route("/whatsapp",methods=['GET', 'POST'])
def reply():
    
    client = Client(account_sid,auth_token)
    message_body = request.form['Body']
    process = Popen(message_body.split(),stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

    message = client.messages.create(body= stdout,from_=sender,to=receiver)
   
    return ";"


if __name__ == '__main__':
	app.run(debug=True)