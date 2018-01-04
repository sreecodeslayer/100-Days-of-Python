from flask_restful import Resource
from flask import request, jsonify, make_response

from mongoengine.errors import DoesNotExist
from base64 import b16encode
from uuid import uuid4

from ecommerce.models.orders import Cart as CartModel
from ecommerce.models.orders import Order as OrderModel
from ecommerce.models.accounts import User as UserModel
from ecommerce.models.accounts import Address as AddressModel
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
						cart.update(dec__total = itm_price, pull__items = itm)


						if item_total > 0:
							cart.update(inc__total = item_total, add_to_set__items = item)

			except DoesNotExist:
				cart.update(inc__total = item_total, add_to_set__items = item)

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


class Checkout(Resource):
	def post(self):
		data = request.get_json()

		try:
			access_key = data.get('access_key')
			billing_addr = data.get('bill_for')

			assert access_key
			assert billing_addr
			
			shipping_addr = data.get('ship_to',billing_addr)

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
			cart = CartModel.objects.get(customer = customer)
		except DoesNotExist:
			return make_response(
				jsonify(message = "Not found"),
				404
			)

		if not cart.items:
			return make_response(
				jsonify(message = "Cart is empty, consider shopping..."),
				404
			)

		oid = "OD#"+str(b16encode(uuid4().bytes),encoding='utf-8')
		

		try:
			shipping_addr = AddressModel.objects.get(aid = shipping_addr)
			billing_addr = AddressModel.objects.get(aid = billing_addr)
			order = OrderModel(oid = oid)
		except DoesNotExist:
			return make_response(
				jsonify(message = "Address(es) Not found"),
				404
			)

		order.customer = customer
		order.shipping_add = shipping_addr
		order.billing_add = billing_addr
		order.items = cart.items
		order.total = cart.total
		order.save()

		order = order.to_mongo().to_dict()
		order.pop("_id")
		order.pop("customer")

		shipping_addr = shipping_addr.to_mongo().to_dict()
		shipping_addr.pop("_id")
		shipping_addr.pop("user")

		billing_addr = billing_addr.to_mongo().to_dict()
		billing_addr.pop("_id")
		billing_addr.pop("user")
		
		order.pop("shipping_add")
		order["ship_to"] = shipping_addr

		order.pop("billing_add")
		order["bill_for"] = billing_addr

		# remove the items from cart
		cart.update(items = [], total = 0)

		return jsonify(order = order)


class Orders(Resource):
	def get(self):
		access_key = request.args.get('access_key')
		page_num = int(request.args.get('page',1))
		per_page = int(request.args.get('per_page',6))


		try:
			assert access_key

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
			ods = OrderModel.objects(
				customer = customer
			).paginate(
				page=page_num,
				per_page=per_page
			)


			_orders = ods.items
			total = ods.total
			total_pages = ods.pages
			current_page = ods.page

			next_page = ods.next_num
			prev_page = ods.prev_num

		except DoesNotExist:
			return make_response(
				jsonify(message = "Not found"),
				404
			)

		orders = []

		try:

			for order in _orders:
				shipping_addr = order.shipping_add.to_mongo().to_dict()
				shipping_addr.pop('_id')
				shipping_addr.pop('user')
				
				billing_addr = order.billing_add.to_mongo().to_dict()
				billing_addr.pop('_id')
				billing_addr.pop('user')


				order = order.to_mongo().to_dict()
				order.pop('_id')
				order.pop('customer')
				order.pop('shipping_add')
				order.pop('billing_add')

				order['ship_to'] = shipping_addr
				order['bill_for'] = billing_addr
				orders.append(order)

			return jsonify(
				orders = orders,
				total = total,
				total_pages = total_pages,
				current_page = current_page,
				next_page = next_page,
				prev_page = prev_page
			)
		except Exception as e:
			raise e


			