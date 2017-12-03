from sanic import Sanic
from sanic.response import json as jsonify
from sanic_jinja2 import SanicJinja2

import requests, asyncio, json

app = Sanic()

app.static('/static', './static')
jinja = SanicJinja2(app)

@app.route("/")
async def index(request):
	return jinja.render('index.html', request)

@app.route("/getData")
async def get_data(request):
	return jsonify({"status":True, "message":"foo:bar"})

@app.websocket("/getRandomAlbum")
async def get_random_album(request, ws):
	try:
		resp = requests.get('https://jsonplaceholder.typicode.com/photos')

		album = resp.json()
		await ws.send(json.dumps({'album':album[0:21], 'status':True}))

	except Exception as e:
		raise e

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000, debug=False)