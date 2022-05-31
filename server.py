
import time

import flask
from flask import Flask, request, redirect, send_from_directory
from twilio.rest import Client
from twilio import twiml
from credentials import * 
from shell import Commander

from gtts import gTTS
from playsound import playsound

app = Flask(__name__,static_folder='voice_notes')
#
#"MediaUrl=https://demo.twilio.com/owl.png"
#

@app.route('/<path:filename>')  
def send_file(filename):  
    return send_from_directory(app.static_folder, filename)


#@app.route('/voice_notes/<path:path>')
#def send_report(path):
#    return send_from_directory('', path)


@app.route("/whatsapp",methods=['GET', 'POST'])
def reply():
    try:
        client = Client(account_sid,auth_token)
        message_body = request.form['Body']
        print (request.form['NumMedia'])
        if request.form['From'] != receiver:
            message = client.messages.create(body="not authenticated",from_=sender,to=request.form['From'])
        
        if message_body[:2].lower() == "vn" and len(message_body) > 2:
            speech = gTTS(text = message_body[2:])    
            fname = 'voice_notes/' + str(time.time()) + ".mp3"
            speech.save(fname)
            media_url = "" + fname
            print (media_url)
            client.messages.create(media_url=media_url,from_=sender,to=request.form['From'])
            return "2"
        #import code; code.interact(local=dict(globals(), **locals()))


        cmd = Commander(message_body)
        cmd.out()
        if cmd.stdout:
             client.messages.create(body="not authenticated",from_=sender,to=request.form['From'])
        if cmd.stderr:
            message = client.messages.create(body=cmd.stderr,from_=sender,to=receiver)
        else:
            message = client.messages.create(body="task completed",from_=sender,to=receiver)
        return ";"
    except Exception as e:
        import code; code.interact(local=dict(globals(), **locals()))


if __name__ == '__main__':
	app.run(debug=True)
