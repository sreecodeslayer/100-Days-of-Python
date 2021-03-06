from flask import Flask
from flask_restful import Api
from ecommerce import settings as SETTINGS
from ecommerce.modules.user import User,Users
from ecommerce.modules.user import Address#,Addresses
from ecommerce.modules.product import Product, Products
from ecommerce.modules.order import Cart, Checkout, Order, Orders

app = Flask(__name__, instance_relative_config=True)
app.config.from_envvar('ECOMMERCE')

# Initialize Flask-Restful
api = Api(app)

# Initialize MongoEngine
ME = SETTINGS.ME
ME.init_app(app)

api.add_resource(User, '/api/user')
api.add_resource(Users, '/api/users')

api.add_resource(Address, '/api/address')
# api.add_resource(Addresses, '/api/addresses')

api.add_resource(Product, '/api/product')
api.add_resource(Products, '/api/products')

api.add_resource(Cart, '/api/cart')
api.add_resource(Checkout, '/api/cart/checkout')
api.add_resource(Order, '/api/manage/order')
api.add_resource(Orders, '/api/orders')
