from app import app
from app import app_loop
import asyncio

server = app.create_server(host="0.0.0.0", port=9000, debug=True)
loop = app_loop
task = asyncio.ensure_future(server)
loop.run_forever()