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
	joined_on = ME.DateTimeField(
		default=datetime.utcnow() + timedelta(hours=5, minutes=30))

	meta = {
		'strict': False,
		'indexes':['email', 'access_key']
	}

	def setpasswd(self, password):
		self.passwd = gen_pass.hash(password)

	def verifypaswd(self, password):
		return gen_pass.verify(password, self.passwd)
