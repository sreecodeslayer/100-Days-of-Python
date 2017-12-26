from flask_mongoengine import MongoEngine
from pymongo import MongoClient
import os

if os.getenv('ECOMMERCE') == 'local.py':
	ME = MongoEngine()
	client = MongoClient()