from flask_restful import Resource
from flask import request, jsonify, make_response
from mongoengine.errors import NotUniqueError, DoesNotExist

from ecommerce.models.accounts import User as UserModel
from ecommerce.models.accounts import Address as AddressModel


class User(Resource):
	def get(self):
		pass

	def post(self):
		data = request.get_json()
		try:
			assert data

			email = data.get('email')
			password = data.get('password')

			assert email and password
		except AssertionError as e:
			return make_response(
				jsonify(message="Invalid request"),
				400
			)

		try:
			user = UserModel(email= email)
			user.setpasswd(password)
			user.save()
			return jsonify(message="Successfully signed up")
			
		except NotUniqueError:
			return make_response(
				jsonify(message = "Email is already taken, consider log-in"),
				422
			)


	def put(self):
		data = request.get_json()
		try:
			assert data

			email = data.get('email')
			password = data.get('password')

			assert email and password
		except AssertionError as e:
			return make_response(
				jsonify(message="Invalid request"),
				400
			)

		try:
			user = UserModel.objects.get(email= email)
			user.setpasswd(password)
			user.save()
			return jsonify(message="Successfully saved the changes")
			
		except Exception as e:
			raise e

	def delete(self):
		data = request.get_json()
		try:
			assert data

			email = data.get('email')
			password = data.get('password')

			assert email and password
		except AssertionError as e:
			return make_response(
				jsonify(message="Invalid request"),
				400
			)

		try:
			user = UserModel.objects.get(email= email)
			user.delete()
		except Exception as e:
			raise e


class Users(Resource):
	def get(self):
		pass

class Address(Resource):
	def get(self):
		pass

	def post(self):
		data = request.get_json()
		try:
			assert data

			full_name = data.get('full_name')
			street_locality = data.get('street_locality')
			city_town = data.get('city_town')
			house_flat = data.get('house_flat')
			country = data.get('country')
			zip_postal = data.get('zip_postal')
			landmark = data.get('landmark')
			phone = data.get('phone')
			access_key = data.get('access_key')


			assert full_name
			assert street_locality
			assert house_flat
			assert city_town
			assert country
			assert zip_postal
			assert phone
			assert access_key
		except AssertionError as e:
			return make_response(
				jsonify(message="Invalid request"),
				400
			)

		try:
			user = UserModel.objects.get(access_key = access_key)
		except DoesNotExist:
			return make_response(
				jsonify(message="Unauthorised"),
				403
			)

		try:
			ad = AddressModel(full_name= full_name)
			ad.user = user
			ad.street_locality = street_locality
			ad.house_flat = house_flat
			ad.city_town = city_town
			ad.country = country
			ad.zip_postal = zip_postal
			ad.landmark = landmark
			ad.phone = phone

			ad.save()

			return jsonify(message="Address added to your address book")
			
		except Exception as e:
			raise e

	def put(self):
		pass

	def delete(self):
		pass



def authorize_access_key(key, role='customer'):
	try:
		user = UserModel.objects.get(access_key = key, role=role)
		return True
	except DoesNotExist:
		return False