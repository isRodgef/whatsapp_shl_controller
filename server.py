import flask
from flask import Flask, request, redirect
from twilio.rest import Client
from twilio import twiml
from credentials import * 
from shell import Commander

app = Flask(__name__)

#def 

@app.route("/whatsapp",methods=['GET', 'POST'])
def reply():
    
    client = Client(account_sid,auth_token)
    message_body = request.form['Body']
    print (request.form['NumMedia'])
    if request.form['From'] != receiver:
        message = client.messages.create(body="not authenticated",from_=sender,to=request.form['From'])

    cmd = Commander(message_body)
    cmd.out()
    if cmd.stdout:
        message = client.messages.create(body=cmd.stdout,from_=sender,to=receiver)
    if cmd.stderr:
        message = client.messages.create(body=cmd.stderr,from_=sender,to=receiver)
    else:
        message = client.messages.create(body="task completed",from_=sender,to=receiver)
    return ";"


if __name__ == '__main__':
	app.run(debug=True)
