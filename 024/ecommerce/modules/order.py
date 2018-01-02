from flask_restful import Resource
from flask import request, jsonify, make_response

from mongoengine.errors import DoesNotExist

from ecommerce.models.orders import Cart as CartModel
from ecommerce.models.accounts import User as UserModel
from ecommerce.models.products import Product as ProductModel
from ecommerce.modules.user import authorize_access_key

class Cart(Resource):
	def get(self):
		access_key = request.args.get('access_key')

		try:
			assert access_key

			if not authorize_access_key(access_key):
				return make_response(
					jsonify(message = "Unauthorised"),
					403
				)
		except AssertionError:
			return make_response(
				jsonify(message = "Invalid request"),
				400
			)

		try:
			customer = UserModel.objects.get(access_key = access_key)
			cart = CartModel.objects.get(customer = customer)
		except DoesNotExist:
			return make_response(
				jsonify(message = "Not found"),
				404
			)

		cart = cart.to_mongo().to_dict()
		cart.pop('customer')
		cart.pop('_id')
		cart = cart.get('items')
		return jsonify(cart = cart)



	def put(self):
		data = request.get_json()

		try:
			access_key = data.get('access_key')
			wanted_items = data.get('items')
		except Exception as e:
			raise e

		if not authorize_access_key(access_key):
			return make_response(
				jsonify(message="Unauthorised"),
				403
			)

		try:
			customer = UserModel.objects.get(access_key = access_key)
			cart = CartModel.objects.get(customer = customer)
		except DoesNotExist:
			cart = CartModel()
			cart.customer = customer
			cart.save()

		current_items = []
		current_total = 0

		for li in wanted_items:
			qty = int(li.get('qty',1))
			pid = li.get('pid', '')
			try:
				product = ProductModel.objects.get(pid = pid)
				item_total = product.price * qty
				
				item = {
					'product':product.pid,
					'name':product.name,
					'qty':qty,
					'rate':product.price,
					'total': item_total
				}

			except DoesNotExist:
				cart.update(items = [])
				cart.update(total = 0)
				return make_response(
					jsonify(message="Product not found: Invalid product added to cart, cart cleared!"),
					404
				)

			try:
				cart = CartModel.objects.get(customer = customer, items__product__in = [pid])
				for itm in cart.items:
					if itm.get('product') == pid:
						itm_price = itm.get('total')
						cart.update(dec__total = itm_price)
						cart.update(inc__total = item_total)

						cart.update(pull__items = itm)

						if item_total > 0:
							cart.update(add_to_set__items = item)

			except DoesNotExist:
				cart.update(inc__total = item_total)
				cart.update(add_to_set__items = item)

		cart.reload()
		cart = cart.to_mongo().to_dict()
		cart.pop('_id')
		cart.pop('customer')
		return jsonify(cart = cart)

	def delete(self):
		data = request.get_json()

		try:
			access_key = data.get('access_key')
			clear = data.get('empty', False)
			pid = data.get('product_id')

			assert access_key
			assert pid

			if not authorize_access_key(access_key):
				return make_response(
					jsonify(message="Unauthorised"),
					403
				)
		except AssertionError:
			return make_response(
				jsonify(message = "Invalid request"),
				400
			)

		try:
			customer = UserModel.objects.get(access_key = access_key)
			cart = CartModel.objects.get(customer = customer, items__product__in = [pid])
		except DoesNotExist:
			return make_response(
				jsonify(message = "Not found"),
				404
			)
		_cart_items = cart.items
		_total = 0

		cart_items = []
		for item in _cart_items:
			if item.get('product') != pid:
				_total += item.get('total')
				cart_items.append(item)
		cart.update(items = cart_items)
		cart.update(total = _total)
		cart.reload()

		total = cart.total
		cart = cart.items
		return jsonify(cart = cart, total = total)