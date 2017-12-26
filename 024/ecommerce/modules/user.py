from flask_restful import Resource
from flask import request, jsonify, make_response
from mongoengine.errors import NotUniqueError

from ecommerce.models.accounts import User as UserModel


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
		pass

	def delete(self):
		pass


class Users(Resource):
	def get(self):
		pass