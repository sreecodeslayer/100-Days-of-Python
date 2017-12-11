from pymongo import MongoClient
import re
from bson import json_util

class Name(object):
	def __init__(self, host="mongodb://localhost:27017",port=27017):
		self.host = host
		self.port = port
		if self.host.startswith("mongodb://"):
			self.client = MongoClient(self.host)

			self.collection = self.client['FIRST_NAMES']['as_of_12_Dec_2017']
		else:
			self.client = MongoClient(host=self.host, port=self.port)

			self.collection = self.client['FIRST_NAMES']['as_of_12_Dec_2017']
		pass

	def getName(self, starts_with='A', meaning=None, gender=None):
		query = {'name':{'$regex':'^%s'%starts_with.capitalize() }}

		if meaning:
			q_string = re.compile('%s'%meaning)
			query['means'] = {'$in':[q_string]}

		if gender:
			if gender.capitalize() in ['Boy','Girl','Unisex']:
				query['gender'] = gender.capitalize()
		cur = self.collection.find(query)
		count = cur.count()
		result = json_util.dumps(cur)

		return result, count