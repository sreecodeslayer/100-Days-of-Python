from sanic.response import json, redirect
from sanic.views import HTTPMethodView
from sanic import Blueprint
# from app import auth

from .models import User

blueprint = Blueprint('SanicScrum', url_prefix = '/')

class Login(HTTPMethodView):
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
				auth.login_user(request, user)
				return redirect('/dashboard')
			return json(
				{"message":"Wrong credential(s)"},
				status = 404
			)

		except Exception as e:
			raise e

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
		email = request.json.get('email')
		phone = request.json.get('phone')
		zone = request.json.get('zone')

		try:
			usr = User(email = email, username = username)
			usr.phone = phone
			usr.zone = zone
			usr.set_passwd(passwd)
			usr.save()

			return json(
				{
				"message":"signup complete for %s and id %s has been assigned"%(
					usr.email,
					usr.id
					)
				}
			)
		except Exception as e:
			raise






