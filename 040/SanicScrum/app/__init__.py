from sanic import Sanic
from sanic.response import redirect

from sanic_auth import Auth
from sanic_jinja2 import SanicJinja2
from sanic_session import RedisSessionInterface

from aoiklivereload import LiveReloader
import asyncio_redis

from app.models import User
import os

name = "SanicScrum"
version = "0.1a"

app_root = os.path.dirname(__file__)
static_root = os.path.join(app_root,'static')
templates_root = app_root
reloader = LiveReloader()
reloader.start_watcher_thread()

app = Sanic(__name__)
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


@app.listener('before_server_start')
async def create_tables(app, loop):
	User.create_table(fail_silently=True)
	

auth = Auth(app)

@auth.serializer
def serializer(user):
	return {'id':str(user.id),'email':user.email,'name':user.username}

@auth.user_loader
def user_loader(user):
	return user


from app.views import Login, Register
from app.views import Dashboard
app.add_route(Login.as_view(),'/login')
app.add_route(Register.as_view(),'/signup')
app.add_route(Dashboard.as_view(),'/dashboard')

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