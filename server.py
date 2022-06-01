
import time

import requests
import flask
from flask import Flask, request, redirect, send_from_directory
from twilio.rest import Client
from twilio import twiml
from credentials import * 
from shell import Commander

from gtts import gTTS


from pydub import AudioSegment
from pydub.silence import split_on_silence

#speech = gTTS(text = "Rodger is Awesome")    
#speech.save('voice_notes/a.mp3')

#https://towardsdatascience.com/easy-speech-to-text-with-python-3df0d973b426
import speech_recognition as sr




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
        #import code; code.interact(local=dict(globals(), **locals()))
        print ("Top of function")
        client = Client(account_sid,auth_token)
        message_body = request.form['Body']
        print (request.form['NumMedia'])
        if request.form['From'] != receiver:
            print ("Why Rodger")
            message = client.messages.create(body="not authenticated",from_=sender,to=request.form['From'])
        
        if 'MediaUrl0' in request.form.keys():
            r = requests.get(request.form['MediaUrl0'])
            if request.form['MediaContentType0'] =='audio/mpeg':
                open('tmp.mp3', 'wb').write(r.content)
                src = 'tmp.mp3'
                sound = AudioSegment.from_mp3(src)
            elif request.form['MediaContentType0'] =='audio/ogg':
                open('tmp.ogg', 'wb').write(r.content)
                src = 'tmp.ogg'
                sound = AudioSegment.from_ogg(src)
            else:
                 message = client.messages.create(body="invalid audio type",from_=sender,to=request.form['From'])
                 return ";"

            sound.export('eg.wav',format="wav")

            r = sr.Recognizer()

            with sr.AudioFile('eg.wav') as source:
                audio_text = r.listen(source)

            try:

                text = r.recognize_google(audio_text)
                client.messages.create(body=text,from_=sender,to=receiver)
                return text
            except Exception as e:
                client.messages.create(body=str(e),from_=sender,to=receiver)
                return str(e)

        if message_body[:2].lower() == "vn" and len(message_body) > 2:
            speech = gTTS(text = message_body[2:])    
            fname = 'voice_notes/' + str(time.time()) + ".mp3"
            speech.save(fname) 
            media_url = "" + fname
            client.messages.create(media_url=  media_url,from_=sender,to=request.form['From'])
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
