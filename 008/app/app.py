from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/profile', methods=['GET', 'POST'])
def function():
	print("Called :: ")
	if request.method == 'GET':
		print("GET :: profile")
		return jsonify(status=True, 
			profile={
			'name':'Sreenadh TC',
			'designation':'Product Engineer',
			'company':'Hashwave Technologies Inc',
			'bio': 'Kannurian | Real Madrid | Photographer | Travel',
			'last_updated': 5
			})
	return jsonify(status=False), 400