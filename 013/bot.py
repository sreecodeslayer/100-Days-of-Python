from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import Updater
from telegram.ext import ConversationHandler
from telegram.ext import CommandHandler, RegexHandler, MessageHandler
from telegram.ext.filters import Filters
from random import choice
from feedparser import parse
import logging
logging.basicConfig(level=logging.INFO,
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger("GameCrack_Bot")

TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
RANDOM_MSGS, FEED_SOURCE = range(2)

FUNNY_REPLIES = [
	'Errm, I am not yet trained to reply to that question',
	'OMKV'
]

def start(bot, update):
	reply_keyboard = [['skidrow']]

	update.message.reply_text(
		'Hi! My name is GameCrack Bot. I will fetch you the latest cracks from your choice.'
		'Send /cancel to stop talking to me.\n\n'
		'Reply your source of crack from these options: [skidrow]',
		reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

	return FEED_SOURCE

def handle_junk(bot, update):
	user = update.message.from_user
	logger.info("User %s has some junk question, %s, give funny replies",
		user.first_name,
		update.message.text
	)
	msg = choice(FUNNY_REPLIES)
	update.message.reply_text(msg)
	return RANDOM_MSGS

def parse_feed(bot, update):
	user = update.message.from_user
	logger.info("User %s asked for feed from %s.",
		user.first_name,
		update.message.text
	)

	asked_for = update.message.text
	if asked_for == 'skidrow':
		message = get_skidrow()
		message = str('\n'.join(message)) if len(message) > 0 else message
		update.message.reply_text(text = message,
			parse_mode='Markdown')
	return ConversationHandler.END
def skidrow(bot, update):
	user = update.message.from_user
	logger.info("User %s asked for feed from %s via command itself.",
		user.first_name,
		update.message.text
	)

	asked_for = update.message.text
	message = get_skidrow()
	message = str('\n'.join(message)) if len(message) > 0 else message
	update.message.reply_text(text = message,
		parse_mode='Markdown')
	return ConversationHandler.END
	
def get_skidrow():
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

	logger.debug("Performing the parsing, getting all feed data...")
	for index,entry in enumerate(entries):
		game = {
			'title': entry.get('title'),
			'link': entry.get('link'),
			'author': entry.get('author'),
			'published': entry.get('published')
		}
		game_str = '''{0}. *Title: {title}*\n
		*Link:* [{link}]({link})\n
		*Author:* _{author}_\n
		*Published:* _{published}_\n'''.format(
			index+1,**game
		)
		games.append(game_str)
	logger.debug("Feed data formatted to a list, returning it to caller...")
	return games



def cancel(bot, update):
	user = update.message.from_user
	logger.info("User %s canceled the conversation.", user.first_name)
	update.message.reply_text(get_bye_msg(),
							  reply_markup=ReplyKeyboardRemove())

	return ConversationHandler.END

def error(bot, update, error):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, error)

def get_bye_msg():
	msgs = [
		'Bye! I hope we can talk again some day.',
		'Ciao',
		'Later!',
		'Bye for now, let\'s talk again']
	return choice(msgs)

def main():
	bot = Updater(TOKEN)
	dispatcher = bot.dispatcher

	conv_handler = ConversationHandler(
		entry_points = [CommandHandler('start', start),CommandHandler('skidrow', skidrow)],
		states = {
		FEED_SOURCE: [RegexHandler('^(skidrow)$', parse_feed)],
		RANDOM_MSGS: [MessageHandler(Filters.text, handle_junk)]
		},
		fallbacks=[CommandHandler('cancel', cancel)]
		)

	dispatcher.add_handler(conv_handler)
	dispatcher.add_error_handler(error)
	bot.start_polling()
	bot.idle()
	logger.info("Bot is up ... awaiting users ...")

if __name__ == '__main__':
	main()