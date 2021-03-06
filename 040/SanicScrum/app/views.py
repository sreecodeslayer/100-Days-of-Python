from sanic.response import json, redirect
from sanic.views import HTTPMethodView
from sanic import Blueprint
from peewee import IntegrityError, DoesNotExist
from app import auth, jinja
from app.models import User, objects
from playhouse.shortcuts import model_to_dict
from playhouse.postgres_ext import ServerSide
from passlib.hash import pbkdf2_sha512


blueprint = Blueprint('SanicScrum', url_prefix = '/')


class Login(HTTPMethodView):

	'''
	Login
	@route: '/login'
	@method: GET

	'''
	async def get(self, request):
		if not auth.current_user(request):
			return jinja.render('login.html', request)
		return redirect('/')
	'''
	Login
	@route: '/login'
	@method: POST
	@params: <username> and <password>
	'''
	async def post(self, request):
		username = request.json.get('username')
		passwd = request.json.get('password')

		try:
			assert username
			assert passwd
		except AssertionError:
			return json(
				{
					"message":"Invalid login request, username and/or password missing"
				},
				status = 401
			)
		try:
			usr = await objects.get(User, username = username)


			if usr and usr.verify_passwd(passwd):
				auth.login_user(request, usr)
				return json(
					{
						'message':"Login success!",
						'user':model_to_dict(usr, 
							backrefs=True,
							exclude={User.passwd, User.id}
						)
					},
					status = 200
				)
			return json(
				{"message":"Wrong credential(s)"},
				status = 404
			)

		except DoesNotExist:
			return json(
				{"message":"No user found with that username"},
				status=404
			)

class Register(HTTPMethodView):
	'''
	Register
	@route: '/signup'
	@method: POST
	@params: <username>, <password>, <email>, <phone>, <zone>
	'''

	async def post(self, request):
		username = request.json.get('username')
		passwd = request.json.get('password')
		email = request.json.get('email','')
		phone = request.json.get('phone','')
		zone = request.json.get('zone','Asia/Kolkata')
		sex = request.json.get('sex','')

		try:
			assert username
			assert passwd
			assert email
			assert phone
			assert zone
			assert sex
		except AssertionError:
			return json(
				dict(message="Invalid request, params missing"),
				status=400
			)

		try:
			usr = await objects.create(
				User,
				email = email,
				username = username,
				phone = phone,
				sex = sex,
				zone = zone,
				passwd = pbkdf2_sha512.hash(passwd)
			)

			return json(
				{
				"message":"signup complete for %s and id %s has been assigned"%(
					usr.email,
					usr.id
					)
				}
			)
		except IntegrityError as e:

			return json(
				dict(message="User already exist with that username and/or email"),
				status=409
			)
		except Exception as e:
			raise

class Dashboard(HTTPMethodView):
	decorators = [auth.login_required]
	async def get(self, request):

		return jinja.render('index.html', request)


class Peoples(HTTPMethodView):
	decorators = [auth.login_required]
	async def get(self, request):
		try:


			usrs = User.select().order_by(User.create_datetime)
			total = await objects.count(usrs)
			usrs = await objects.execute(usrs)
			users = []
			for usr in usrs:
				users.append(model_to_dict(usr, exclude = [User.passwd]))

			return json(
				dict(users = users, total = total)
			)
		except Exception as e:
			raise e

class People(HTTPMethodView):
	decorators = [auth.login_required]
	async def put(self, request):
		try:
			_id = request.json.get('id')
			assert email
			assert _id
		except AssertionError:
			return json(
				dict(
					message="id of the user required to edit him/her"
				),
				status=400
			)
		try:
			email = request.json.get('email')
			username = request.json.get('username')
			phone = request.json.get('phone')
			sex = request.json.get('sex')
		except Exception as e:
			raise e

		try:
			usr = await objects.get(User, id=_id)
			if email:
				usr.email = email
				await objects.update(email)
			if username:
				usr.username = username
				await objects.update(username)
			if phone:
				usr.phone = phone
				await objects.update(phone)
			if sex:
				usr.sex = sex
				await objects.update(sex)

			return json(
				dict(
					message="User with id: %s has been edited"%(id)
				)
			)
		except DoesNotExist:
			return json(
				dict(
					message="User not found in team, sorry!"
					),
				status=404
			)

	async def delete(self, request):
		try:
			email = request.json.get('email')
			assert email
		except AssertionError:
			return json(
				dict(
					message="email of the user required to delete him/her"
				),
				status=400
			)

		try:
			usr = await objects.get(User, email=email)
			result = await objects.delete(usr)

			return json(
				dict(
					message="User with email: %s has been removed from team"%(email)
				)
			)
		except DoesNotExist:
			return json(
				dict(
					message="User not found in team, sorry!"
					),
				status=404
			)

