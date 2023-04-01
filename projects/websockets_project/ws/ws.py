import socketio


sio_server = socketio.AsyncServer(
    async_mode = 'asgi'
)

sio_app = socketio.ASGIApp(
    socketio_server = sio_server,
    socketio_path = 'ws'
)

@sio_server.event
def connect(sid, environ, auth):
    print('connection established')
    
@sio_server.event
def take_case(sid, data):
    # with open
    pass

@sio_server.event
async def on_data(sid, data):
    print('message received with ', data)
    await sio_server.emit('on_data', {'response': data}, namespace=sid)

@sio_server.event
def disconnect(sio):
    print('disconnected from server')