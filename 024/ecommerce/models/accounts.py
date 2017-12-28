from datetime import datetime, timedelta
from passlib.hash import pbkdf2_sha512 as gen_pass
from uuid import uuid4

from ecommerce import settings as SETTINGS


ME= SETTINGS.ME

class User(ME.Document):
	email = ME.EmailField(unique=True)
	passwd = ME.StringField()
	username = ME.StringField()
	access_key = ME.StringField(default = uuid4().hex)
	role = ME.StringField(max_length=10, default='customer')
	joined_on = ME.DateTimeField(
		default=datetime.utcnow() + timedelta(hours=5, minutes=30))

	meta = {
		'strict': False,
		'indexes':['email', 'access_key']
	}

	def setrole(self, role):
		self.role = role

	def setpasswd(self, password):
		self.passwd = gen_pass.hash(password)

	def verifypaswd(self, password):
		return gen_pass.verify(password, self.passwd)

class Address(ME.Document):
	user = ME.ReferenceField(User)
	full_name = ME.StringField(required=True)
	house_flat = ME.StringField(required=True)
	street_locality = ME.StringField(required=True)
	city_town = ME.StringField(required=True)
	country = ME.StringField(required=True)
	landmark = ME.StringField()
	type = ME.StringField(default='home')
	zip_postal = ME.StringField()
	phone = ME.StringField()
	aid = ME.UUIDField(default=uuid4, binary=False)

	meta = {
		'strict':False
	}