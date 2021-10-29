import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from pythonREPL import execute_python

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
	incoming_msg = request.values.get('Body', '').lower()
	resp = MessagingResponse()
	msg = resp.message()

	print(incoming_msg)
	if incoming_msg.startswith('#!python3'):
		code = incoming_msg.lstrip('#!python3')
		print(code)
		output = execute_python(code)
		print(output)
		msg.body(output)

	return str(resp)

if __name__ == '__main__':
	app.run()