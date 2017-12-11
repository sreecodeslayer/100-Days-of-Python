from flask import Flask, request, jsonify
from name import Name
import json 

app = Flask(__name__)

@app.route('/name',methods=['GET'])
def get_name():
	try:
		starts_with = request.args.get('starts_with')
		gender = request.args.get('gender')
		means = request.args.get('means')
	except Exception as e:
		raise e

	try:
		name = Name()
		(result, count) = name.getName(
			starts_with=starts_with,
			gender=gender,
			meaning=means
			)
		result = json.loads(result)
		print(type(result))
		return jsonify(status= True, count= count, result=result)
	except Exception as e:
		raise e