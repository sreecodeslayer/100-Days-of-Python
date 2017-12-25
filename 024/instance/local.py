from flask_mongoengine import MongoEngine

DEBUG = True
TESTING = False

MONGODB_SETTINGS = [
	{
		'db'	:	'ECOMMERCE'  ,
		'host'	:	'localhost',
		'port'	:  27017
	}
]


ME = MongoEngine()