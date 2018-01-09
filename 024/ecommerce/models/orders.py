from uuid import uuid4
from base64 import b16encode
from datetime import datetime, timedelta

from ecommerce import settings as SETTINGS
from ecommerce.models.accounts import User as UserModel
from ecommerce.models.accounts import Address as AddressModel
from ecommerce.models.products import Product as ProductModel

ME = SETTINGS.ME

class Cart(ME.Document):
	customer = ME.ReferenceField(UserModel)
	items = ME.ListField()
	total = ME.FloatField(default=0)

class Shipment(ME.Document):
	shipped_on = ME.DateTimeField(
		default=datetime.utcnow() + timedelta(hours=5, minutes=30)
	)
	status = ME.StringField()
	awb = ME.StringField()
	track_here = ME.URLField()
	delivered_on = ME.DateTimeField()

class Order(ME.Document):
	oid = ME.StringField()
	ordered_on = ME.DateTimeField(
		default=datetime.utcnow() + timedelta(hours=5, minutes=30)
	)
	shipped_on = ME.DateTimeField()
	items = ME.ListField(default = [])
	total = ME.FloatField(default = 0)
	paid = ME.BooleanField(default=False)
	billing_add = ME.ReferenceField(AddressModel)
	shipping_add = ME.ReferenceField(AddressModel)
	status = ME.StringField(default="Awaiting Payment")
	shipment = ME.ReferenceField(Shipment)
	meta = {
		'strict':False,
		'indexes':['oid','ordered_on']
	}
