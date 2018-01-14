from peewee import PostgresqlDatabase, Model
from peewee import CharField, TextField, DateTimeField
from passlib.hash import pbkdf2_sha512
from datetime import datetime
psql_db = PostgresqlDatabase('sanic_scrum', user='sanic_scrum')


class BaseModel(Model):
	"""A base model that will use our Postgresql database"""
	class Meta:
		database = psql_db

class User(BaseModel):

	create_datetime = DateTimeField(default=datetime.utcnow(), null=True)
	username = CharField(unique = True, index = True)
	passwd = CharField()
	email = CharField(unique = True, index = True)
	phone = CharField()
	sex = CharField()
	zone = TextField()

	def verify_passwd(self, passwd):
		return pbkdf2_sha512.verify(passwd, self.passwd)

	def set_passwd(self, passwd):
		self.passwd = pbkdf2_sha512.hash(passwd)

