# whatsapp_shl_controller
Basic reverse shell that will be controlled through whatsapp using the twilio whatsapp api
but 
I created this program when I wanted to control my computer from my phone, so I decided to use whatsapp. I used twilio to handle (with ngrok port forwarding) the sending of whatsapp messages to flask server.

Possible Use Cases

system monitoring while away from computer during lunch.

In order to use this you need to have a twilio account.

You will need to update credenials.py 

* sender = twilio number
* receiver = number of phone that send shell commands
* account_sid will get this from twilio
* auth_token recived from twilio
