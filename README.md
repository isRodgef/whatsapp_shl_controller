# whatsapp_shl_controller
Basic reverse shell that will be controlled through whatsapp using the twilio whatsapp api

I created this program when I wanted to control my computer from my phone, so I decided to use whatsapp. I used twilio to handle (with ngrok port forwarding) the sending of whatsapp messages to flask server.

Possible Use Cases

*system monitoring while away from computer
*remote git pushes
*checking if computer is still on

In order to use this you need to have a twilio account.

Have the server running I use ngrok for port forwarding.

You will need to update credenials.py 

* sender = twilio number
* receiver = number of phone that send shell commands
* account_sid will get this from twilio
* auth_token recived from twilio

I also added text to speech
* Send text back get a voice note
* Send voice note get text back