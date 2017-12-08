from datetime import datetime, timedelta
from threading import Lock
from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, join_room, leave_room
from uuid import uuid4
from random import randint

import time

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None
thread_lock = Lock()
async_mode = None

clients_connected = []

def background_timer(sid):
	while True:
		time.sleep(1)
		t = str(datetime.utcnow() + timedelta(hours=5, minutes=30))
		socketio.emit('time', {'data': 'This is data',
							'time': t}, namespace='/vue', room=sid)


@app.route('/')
def index():
	return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on('connect', namespace='/vue')
def connected():
	clients_connected.append(request.sid)
	room = session.get('room')
	join_room(room)
	print("Client connected ... ", clients_connected, room)
	socketio.emit('message', {'data': 'Connected', 'count': 0}, room=request.sid)
	global thread
	with thread_lock:
		if thread is None:
			thread = socketio.start_background_task(background_timer,*[request.sid])

@socketio.on('disconnect', namespace='/vue')
def disconnected():
	clients_connected.remove(request.sid)
	room = session.get('room')
	leave_room(room)
	# Clean all the threads on client disconnects
	global thread
	if thread is not None:
		thread.kill()
		thread = None
	print('Client disconnected')

@socketio.on('uuid', namespace='/vue')
def send_uuid():
	print("UUID :: ")
	socketio.emit('uuid', {'uuid': str(uuid4())}, namespace='/vue', room=request.sid)

@socketio.on('hex', namespace='/vue')
def send_hex():
	socketio.emit('hex', {'hex': str(uuid4().hex)}, namespace='/vue', room=request.sid)


if __name__ == '__main__':
	socketio.run(app, debug=True, port=8000)