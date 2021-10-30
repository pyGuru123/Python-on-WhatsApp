import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from pythonREPL import execute_python, install_package

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
	incoming_msg = request.values.get('Body', '').strip()
	print(incoming_msg)
	resp = MessagingResponse()
	msg = resp.message()

	if incoming_msg.startswith('#!python3'):
		code = incoming_msg.lstrip('#!python3')
		output = execute_python(code)
		msg.body(output)

	elif incoming_msg.startswith('!pip install'):
		package = incoming_msg.split()[-1]
		output = install_package(package)
		msg.body(output)

	return str(resp)

if __name__ == '__main__':
	app.run()