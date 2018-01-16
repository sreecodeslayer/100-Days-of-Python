from sanic import Sanic
from app.models import User
from sanic_auth import Auth
from aoiklivereload import LiveReloader
from sanic_session import RedisSessionInterface
import asyncio_redis
name = "SanicScrum"
version = "0.1a"


reloader = LiveReloader()
reloader.start_watcher_thread()

app = Sanic(__name__)
app.config.AUTH_LOGIN_URL = '/'

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
	print(request.headers)
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


app.auth = auth


from app.views import Login, Register
from app.views import Dashboard
app.add_route(Login.as_view(),'/login')
app.add_route(Register.as_view(),'/signup')
app.add_route(Dashboard.as_view(),'/dashboard')
