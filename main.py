import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from src.pythonREPL import execute_python, install_package
import src.services as services

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
	incoming_msg = request.values.get('Body', '').strip()
	isPythonCode = False
	resp = MessagingResponse()
	msg = resp.message()

	if incoming_msg.startswith('#!python3'):
		code = incoming_msg.lstrip('#!python3')
		output = execute_python(code)
		msg.body(output)
		isPythonCode = True

	elif incoming_msg.startswith('!pip install'):
		package = incoming_msg.split()[-1]
		output = install_package(package)
		msg.body(output)
		isPythonCode = True

	if isPythonCode:
		return str(resp)

	incoming_msg = incoming_msg.lower()

	if 'date' in incoming_msg:
		output = services.get_date()
		msg.body(output)

	elif 'time' in incoming_msg:
		output = services.get_time()
		msg.body(output)

	elif 'joke' in incoming_msg:
		output = services.get_joke()
		msg.body(output)

	elif 'quote' in incoming_msg:
		output = services.get_quote()
		msg.body(output)

	return str(resp)

if __name__ == '__main__':
	app.run()