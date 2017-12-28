from uuid import uuid4
from base64 import b16encode

from ecommerce import settings as SETTINGS
from ecommerce.models.accounts import User


ME = SETTINGS.ME

class Product(ME.Document):
	name = ME.StringField()
	pid = ME.StringField(
		default = str(b16encode(
			uuid4().bytes),encoding='utf-8')
		)
	desc = ME.StringField()
	available_stock = ME.IntField()
	price = ME.FloatField()
	sellers = ME.ListField(ME.ReferenceField(User))
	image_urls = ME.ListField()

	meta = {
		'strict':False,
		'indexes':['pid']
	}