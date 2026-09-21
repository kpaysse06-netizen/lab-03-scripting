
#!/Library/Frameworks/Python.framework/Versions/3.15/bin/python3

import os
import json
import requests

GHUSER = os.getenv('GHUSER')
url = f'https://api.github.com/users/{GHUSER}/events'
def retrieve_events(url):
	"""Retrieves information and details about events"""
	text =requests.get(url).text
	events = json.loads(text)
	return events
def print_events(events, n=5):
	"""Prints the first specified items in an event and type and repository"""
	for x in events[:n]:
    		event = x['type'] + ' :: ' + x['repo']['name']
    		print(event)
def main():
	print(GHUSER)
	print(url)
	events=retrieve_events(url)
	print_events(events)

if __name__ == "__main__":
    main()
