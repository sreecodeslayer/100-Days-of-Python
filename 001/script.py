'''
Make OOP based script that gets the current Weather automatically
'''

import requests
import logging
import sys

logger = logging.getLogger('WeatherApp')

ch = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
	'%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)


class Weather(object):

	def __init__(self):
		super(Weather, self).__init__()

		try:
			response = requests.get('http://ip-api.com/json')
			self.APPID = '53d1d372a980abf35de3df940725a82e'
			self.current_location = {
				'lat': response.json().get('lat'),
				'lon': response.json().get('lon'),
				'city': response.json().get('city'),
				'regionName': response.json().get('regionName'),
				'country': response.json().get('country')
			}
		except requests.exceptions.ConnectionError as e:
			self.current_location = {}
			logger.error(str(e))

	def get_weather(self):
		if self.current_location:
			logger.debug("Your Current Location, {city}, lat {lat} : lon {lon}".format(
				**self.current_location))

			query = 'http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&APPID=%s' % (
					self.current_location.get('lat'),
					self.current_location.get('lon'),
					self.APPID)

			logger.debug("[Sending request : %s]" % (query))
			try:
				response = requests.get(query)
				logger.debug("[Response %s : %s]" %
							 (response.status_code, response.url))
				data = response.json()
			except requests.exceptions.ConnectionError as e:
				logger.error(str(e))

			logger.info("Current weather in {},{},{} is {}F, {}% humid".format(
				self.current_location.get('city'),
				self.current_location.get('regionName'),
				self.current_location.get('country'),
				data.get('main').get('temp'),
				data.get('main').get('humidity')
			)
			)
			logger.info("Bye!")
		else:
			logger.error(
				"Could not fetch your current location, are you connected to the web!?")
			logger.error("Bye!")
try:
	w = Weather()
	w.get_weather()
except Exception as e:
	logger.error("Something unexpected happened!")
	logger.exception(e)
