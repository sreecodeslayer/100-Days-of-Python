from sanic import Sanic
from sanic.response import redirect

from sanic_auth import Auth
from sanic_jinja2 import SanicJinja2
from sanic_session import RedisSessionInterface

from peewee import IntegrityError, DoesNotExist
from peewee_async import Manager

from uuid import uuid4
from aoiklivereload import LiveReloader


import asyncio
import asyncio_redis
import os

name = "SanicScrum"
version = "0.1a"

current_admin_passwd = "5379ae883dfb46e18694"

app_root = os.path.dirname(__file__)
static_root = os.path.join(app_root,'static')
templates_root = app_root
reloader = LiveReloader()
reloader.start_watcher_thread()

app = Sanic(__name__)
app_loop = asyncio.get_event_loop()

app.static('/static', static_root)
app.static('/templates', templates_root)
app.config.AUTH_LOGIN_URL = '/'

jinja = SanicJinja2(app)

class Redis:
	"""
	A simple wrapper class that allows you to share a connection
	pool across your application.
	"""
	_pool = None

	async def get_redis_pool(self):
		if not self._pool:
			self._pool = await asyncio_redis.Pool.create(
				host='localhost', port=6379, poolsize=10
			)

		return self._pool


redis = Redis()


# pass the getter method for the connection pool into the session
# https://pythonhosted.org/sanic_session/using_the_interfaces.html
session = RedisSessionInterface(redis.get_redis_pool, cookie_name="session")

@app.middleware('request')
async def add_session_to_request(request):
	await session.open(request)

@app.middleware('response')
async def save_session(request, response):
	await session.save(request, response)



from app.models import User

@app.listener('before_server_start')
async def create_tables(app, loop):
	# Create table if not present
	User.create_table(fail_silently=True)

	# Create admin user if not present
	try:	
		usr = User(email = "admin@sanic_scrum.io", username = "admin")
		usr.sex = ""
		usr.phone = ""
		usr.zone = ""

		new_passwd = uuid4().hex[:20]
		usr.set_passwd(new_passwd)
		usr.save()

		print("="*50)
		print("Admin credentials generated\n")
		print("Username: admin\nPassword: {}".format(new_passwd))
		print("="*50)
	except IntegrityError:

		print("="*50)
		print("Admin credentials are already created.\nPlease use them to login as admin")
		print("="*50)

auth = Auth(app)

@auth.serializer
def serializer(user):
	return {'id':str(user.id),'email':user.email,'name':user.username}

@auth.user_loader
def user_loader(user):
	return user


from app.views import Login, Register
from app.views import Dashboard, Peoples, People
app.add_route(Login.as_view(),'/login')
app.add_route(Register.as_view(),'/signup')
app.add_route(Dashboard.as_view(),'/dashboard')
app.add_route(Peoples.as_view(),'/users')
app.add_route(People.as_view(),'/user')

@app.route('/logout', methods=['GET'])
@auth.login_required
async def logout(request):
	auth.logout_user(request)
	return redirect('/')

@app.route('/', methods=['GET'])
async def index(request):
	if auth.current_user(request):
		return redirect('/dashboard')
	return redirect('/login')