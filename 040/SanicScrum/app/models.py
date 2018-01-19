from peewee import Model
from playhouse.postgres_ext import PostgresqlExtDatabase
from peewee import CharField, TextField, DateTimeField
from peewee_async import Manager, PostgresqlDatabase

from passlib.hash import pbkdf2_sha512
from datetime import datetime

from app import app_loop

# psql_db = PostgresqlExtDatabase('sanic_scrum', user='sreenadh', register_hstore=False)
psql_db = PostgresqlDatabase(database = 'sanic_scrum', user='sreenadh')


objects = Manager(psql_db, loop=app_loop)

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

