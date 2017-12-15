from flask import Flask, request, jsonify
from flask import redirect, url_for

from flask_mongoengine import MongoEngine
from mongoengine.errors import DoesNotExist,NotUniqueError

from flask_security import Security, MongoEngineUserDatastore
from flask_security import UserMixin, RoleMixin, login_required
from flask_security import login_user, current_user, logout_user

from passlib.hash import pbkdf2_sha512 as sha

from datetime import datetime, timedelta

# Create app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'

# MongoDB Config
app.config['MONGODB_DB'] = 'flask_security_app'
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017
app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'
app.config['WTF_CSRF_ENABLED'] = False
# Create database connection object
db = MongoEngine(app)

class Role(db.Document, RoleMixin):
	name = db.StringField(max_length=80, unique=True)
	description = db.StringField(max_length=255)

class User(db.Document, UserMixin):
	email = db.StringField(max_length=255, unique=True)
	password = db.StringField(max_length=255)
	active = db.BooleanField(default=True)
	roles = db.ListField(
		db.ReferenceField(Role),
		default=[]
	)
	confirmed_at = db.DateTimeField(
		default= datetime.utcnow() + timedelta(hours = 5, minutes = 30)
	)

	def set_password(self, password):
		self.password = sha.hash(password)

	def verify_password(self, password):
		return sha.verify(password, self.password) 



# Setup Flask-Security
user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create all basic roles for the app
@app.before_first_request
def create_roles():
	try:
		# Basic routes, user
		user_datastore.create_role(name="User")
	except NotUniqueError:
		pass
	try:
		# Supervisor of users, control
		user_datastore.create_role(name="Admin")
	except NotUniqueError:
		pass
	try:
		# EVERY ACCESS
		user_datastore.create_role(name="God")
	except NotUniqueError:
		pass

# Views
@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	email = data.get('email')
	try:
		user = User(email=email)
		user.save()
	except NotUniqueError:
		return jsonify(status=False, message="Email already taken")

	password = data.get('password')
	user.set_password(password)
	user.save()
	return jsonify(
		status=True,
		user=str(user.id),
		message="Registration success!"
	)

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')

	try:
		user = User.objects.get(email=email)
	except DoesNotExist:
		return jsonify(status=False, message="user not found")

	if user.verify_password(password):
		login_user(user)
		return redirect(url_for('home'))
	

@app.route('/')
def home():
	if current_user.is_authenticated:
		user = {
			'email':current_user.email,
			'confirmed_at':current_user.confirmed_at
		}
		return jsonify(user = user, status=True)
	return jsonify(user = None, status=False)

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=6677)