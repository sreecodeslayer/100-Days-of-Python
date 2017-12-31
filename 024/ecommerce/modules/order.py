from flask_restful import Resource
from flask import request, jsonify, make_response

from mongoengine.errors import DoesNotExist

from ecommerce.models.orders import Cart as CartModel
from ecommerce.models.accounts import User as UserModel
from ecommerce.models.products import Product as ProductModel
from ecommerce.modules.user import authorize_access_key

class Cart(Resource):
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
			except DoesNotExist:
				cart.update(items = [])
				cart.update(total = 0)
				return make_response(
					jsonify(message="Product not found: Invalid product added to cart, cart cleared!"),
					404
				)

			item_total = product.price * qty
			current_total += item_total

			cart.reload()
			if cart.items:
				for curr in cart.items:
					if curr['product'] == product.pid:
						curr['qty'] = qty
						curr['total'] = item_total
						print("If >> ", curr)
						current_items.append(curr)
			else:
				item = {
					'product':product.pid,
					'name':product.name,
					'qty':qty,
					'rate':product.price,
					'total': item_total
				}
				current_items.append(item)

		cart.update(items = current_items)
		cart.update(total = current_total)

		cart.reload()
		cart = cart.to_mongo().to_dict()
		cart.pop('_id')
		cart.pop('customer')
		return jsonify(cart = cart)
		