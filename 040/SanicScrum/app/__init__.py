from sanic import Sanic
from app.views import blueprint, Login, Register
from app.models import *
from sanic_auth import Auth

name = "SanicScrum"
version = "0.1a"

app = Sanic(__name__)
app.config.AUTH_LOGIN_ENDPOINT = 'login'

auth = Auth(app)

app.add_route(Login.as_view(),'/login')
app.add_route(Register.as_view(),'/signup')
# app.blueprint(blueprint)