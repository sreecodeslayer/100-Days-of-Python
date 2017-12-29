from uuid import uuid4
from base64 import b16encode
from datetime import datetime, timedelta

from ecommerce import settings as SETTINGS
from ecommerce.models.accounts import User as UserModel
from ecommerce.models.accounts import Address as AddressModel
from ecommerce.models.products import Product as ProductModel


class Cart(ME.Document):
	customer = ME.ReferenceField(UserModel)
	items = ME.DictField()
	total = ME.FloatField()

class Shipment(ME.Document):
	shipped_on = ME.DateTimeField(
		default=datetime.utcnow() + timedelta(hours=5, minutes=30)
	)
	status = ME.StringField()
	awb = ME.StringField()
	track_here = ME.URLField()
	delivered_on = ME.DateTimeField()

class Order(ME.Document):
	oid = ME.StringField(
		default = "OD#"+str(b16encode(
			uuid4().bytes),encoding='utf-8')
		)

	shipped_on = ME.DateTimeField(
		default=datetime.utcnow() + timedelta(hours=5, minutes=30)
	)

	total = ME.FloatField()
	paid = ME.BooleanField(default=False)
	billing_add = ME.ReferenceField(AddressModel)
	selling_add = ME.ReferenceField(AddressModel)
	status = ME.StringField(default="Awaiting Payment")
	shipment = ME.ReferenceField(Shipment)
	meta = {
		'strict':False,
		'indexes':['oid']
	}
