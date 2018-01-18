from sanic.response import json, redirect
from sanic.views import HTTPMethodView
from sanic import Blueprint
from peewee import IntegrityError, DoesNotExist
from app import auth, jinja
from app.models import User
from playhouse.shortcuts import model_to_dict


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
			usr = User.get(username = username)

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
			usr = User(email = email, username = username)
			usr.phone = phone
			usr.sex = sex
			usr.zone = zone
			usr.set_passwd(passwd)
			usr.save()

			print(usr)

			return json(
				{
				"message":"signup complete for %s and id %s has been assigned"%(
					usr.email,
					usr.id
					)
				}
			)
		except IntegrityError:
			return json({
				"message":"User already exist with that username and/or email"
			})
		except Exception as e:
			raise

class Dashboard(HTTPMethodView):
	decorators = [auth.login_required]
	async def get(self, request):

		return json({"message":"Dashboard"})





