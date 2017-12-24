from smtplib import SMTP_SSL
from smtplib import SMTPAuthenticationError
from feedparser import parse

import os

MAILING_LIST = "mailing_list.txt"

HOST = 'xxxxxxxxxxxxxxxx'
PORT = 000
USER = 'xxxxxxxxxxxxxxxx'
PASSWORD = 'xxxxxxxxxxxxxxxx'



MAILING_LIST= os.path.join(os.path.dirname(__file__), MAILING_LIST)

smtp = SMTP_SSL(host=HOST, port=PORT)
try:
	smtp.login(USER, PASSWORD)
except SMTPAuthenticationError as e:
	print(e)



def get_feed():
	url = 'http://feeds.feedburner.com/SkidrowReloadedGames'
	games = []

	feed = parse(url)
	# feed is dict_items
	feed_items = list(feed.items())

	'''
	You could sort the list and brace that the feed format doesn't
	change, but I chose to loop.
	'''

	for item in feed_items:
		if item[0] == 'entries':
			entries = item[1]
			break

	for entry in entries:
		games.append(entry.get('link'))

	return games


with open(MAILING_LIST, "r") as mail_file:
	games = get_feed()
	games = '\n'.join(games)

	msg = "Hi,\nHere are the latest updates from SkidrowReloadedGames:\n" + games
	print("email this .... \n",msg)

	for email in mail_file:
		smtp.sendmail(SENDER_EMAIL, email, msg)
