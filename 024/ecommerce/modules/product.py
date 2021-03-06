from flask_restful import Resource
from flask import request, make_response, jsonify

from mongoengine.errors import DoesNotExist

from ecommerce.models.products import Product as ProductModel
from ecommerce.models.accounts import User as UserModel
from ecommerce.modules.user import authorize_access_key


class Product(Resource):
	def post(self):
		data = request.get_json()
		try:
			access_key = data.get('access_key')
			name = data.get('name')
			available_stock = data.get('available_stock')
			price = data.get('price')
			desc = data.get('desc')
			sellers = data.get('sellers')
			image_urls = data.get('img_urls')

			assert access_key
			assert name
			assert available_stock
			assert price
			assert desc
			assert sellers
		except AssertionError:
			return make_response(
				jsonify(message="Invalid request"),
				400
			)

		if not authorize_access_key(access_key, role="seller"):
			return make_response(
				jsonify(message="Unauthorised"),
				403
			)
		else:

			_sellers = sellers.split(',')

			sellers = []
			image_urls = image_urls.split(',')
			for seller in _sellers:
				try:
					user = UserModel.objects.get(email = seller)
				except DoesNotExist:
					return make_response(
						jsonify(message="Seller with email: %s not found"%(seller)),
						404
					)

				sellers.append(user)

			try:
				pd = ProductModel(name = name)
				pd.available_stock = available_stock
				pd.price = price
				pd.pid = str(b16encode(uuid4().bytes),encoding='utf-8')
				pd.desc = desc
				pd.sellers = sellers
				pd.image_urls = image_urls
				pd.save()
			except Exception as e:
				raise e

			return jsonify(message = "Product added!")

	def put(self):
		data = request.get_json()
		try:
			access_key = data.get('access_key')
			pid = data.get('product_id')
			name = data.get('name')
			available_stock = data.get('available_stock')
			price = data.get('price')
			desc = data.get('desc')
			sellers = data.get('sellers')
			image_urls = data.get('img_urls')

			assert access_key
			assert pid
		except AssertionError:
			return make_response(
				jsonify(message="Invalid request"),
				400
			)

		if not authorize_access_key(access_key, role="seller"):
			return make_response(
				jsonify(message="Unauthorised"),
				403
			)
		else:

			_sellers = sellers.split(',')

			sellers = []
			image_urls = image_urls.split(',')
			for seller in _sellers:
				try:
					user = UserModel.objects.get(email = seller)
				except DoesNotExist:
					return make_response(
						jsonify(message="Seller with email: %s not found"%(seller)),
						404
					)

				sellers.append(user)

			try:
				pd = ProductModel.objects.get(pid = pid)
				pd.update(name = name)
				pd.update(available_stock = available_stock)
				pd.update(price = price)
				pd.update(desc = desc)
				pd.update(add_to_set__sellers = sellers)
				pd.update(add_to_set__image_urls = image_urls)
			except Exception as e:
				raise e

			return jsonify(message = "Product updated!")


class Products(Resource):
	def get(self):
		try:
			page_num = int(request.args.get('page',1))
			per_page = int(request.args.get('per_page',6))
			pds = ProductModel.objects.paginate(page=page_num, per_page=per_page)

			_products = pds.items
			total = pds.total
			total_pages = pds.pages
			current_page = pds.page

			next_page = pds.next_num
			prev_page = pds.prev_num

			products = []
			for product in _products:
				sellers = [{'email':s.email,'name':s.username} for s in product.sellers]
				p = product.to_mongo().to_dict()
				p['sellers'] = sellers
				p['available_stock'] = product.available_stock if product.available_stock < 5 else True
				p.pop('_id')
				products.append(p)

			return jsonify(
				products=products,
				total=total,
				total_pages=total_pages,
				next_page=next_page,
				prev_page=prev_page
			)

		except Exception as e:
			raise e