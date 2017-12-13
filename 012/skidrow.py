from feedparser import parse

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
		game = {
			'title': entry.get('title'),
			'link': entry.get('link'),
			'author': entry.get('author'),
			'published': entry.get('published')
		}
		games.append(game)

	return games
