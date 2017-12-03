from sanic import Sanic
from sanic.response import json
from sanic_jinja2 import SanicJinja2
app = Sanic()

app.static('/static', './static')
jinja = SanicJinja2(app)

@app.route("/")
async def test(request):
	return jinja.render('index.html', request)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000)