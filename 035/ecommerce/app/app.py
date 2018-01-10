from flask import Flask, make_response
from flask import request, render_template, jsonify
from flask_mongoengine import MongoEngine
from mongoengine.errors import DoesNotExist

from flask_login import UserMixin, LoginManager
from flask_login import login_required, login_user
from flask_login import current_user

from datetime import datetime, timedelta
from uuid import uuid4
from pymongo import MongoClient
from functools import wraps

import os, requests

app = Flask(__name__)


if os.getenv('ECOMMERCE') == 'local.py':
	ME = MongoEngine()
	client = MongoClient()
	master_api = "http://localhost:6677/api"

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
	
	def get_role(self):
		return self.role

	# Flask - Login funcs
	def __unicode__(self):
		return self.id

	def is_authenticated(self):
		return True

	def get_id(self):
		return str(self.id)

	def is_active(self):
		return True

	def is_anonymous(self):
		return False


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user):
	return User.objects.get(id=user)

def login_required(role="customer"):
	def wrapper(fn):
		@wraps(fn)
		def decorated_view(*args, **kwargs):

			if not current_user.is_authenticated():
				return login_manager.unauthorized()
			urole = login_manager.reload_user().get_role()
			if ( (urole != role) and (role != "customer")):
				return login_manager.unauthorized()      
			return fn(*args, **kwargs)
		return decorated_view
	return wrapper

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	try:
		email = data.get('email')
		password = data.get('password')

		assert email
		assert password
	except AssertionError:
		return make_response(
			jsonify(message="Invalid request"),
			400
		)
	try:
		user = User.objects.get(email = email)
	except DoesNotExist:
		return make_response(
			jsonify(message = "Email not found, please signup"),
			404
		)
	if user.verifypaswd(password):
		login_user(user)
	else:
		return jsonify(message="Wronng credentials")

@app.route('/')
def index():
	try:
		if current_user.get_role() == 'customer':
			return render_template('index.html')
		elif current_user.get_role() == 'seller':
			return "Seller"
	except AttributeError:
		return render_template('login.html')

@app.route('/seller', methods = ['GET'])
@login_required(role='seller')
def seller():
	return current_user.to_mongo().to_dict()

@app.route('/products', methods=['GET'])
def products():
	page = request.args.get('page')
	per_page = request.args.get('per_page')

	payload = {
		'page':page,
		'per_page':per_page
	}
	
	try:
		response = requests.get(master_api+'/products', data = payload)
	except Exception as e:
		raise e
		
	return response.json()

if __name__ == '__main__':
	app.run()