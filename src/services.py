import os
import requests
import datetime

def get_date():
	dt = datetime.datetime.now()
	dt = dt.date()
	return dt.strftime('%B %d, %Y')

def get_time():
	dt = datetime.datetime.now()
	dt = dt.time()
	return dt.strftime('%I:%M %p')

def get_joke():
	url = 'https://some-random-api.ml/joke'
	r = requests.get(url)
	data = r.json()
	return data['joke']