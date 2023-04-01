import socketio
import asyncio

# asyncio
sio = socketio.AsyncClient()

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error(data):
    print("The connection failed!")
    
@sio.event
async def on_data(data):
    print(f"The data is {data}")
    await sio.disconnect()
    
@sio.event
def disconnect():
    print("I'm disconnected!")
    
is_connected = True
async def main():
    await sio.connect('http://localhost:8000', socketio_path='ws', wait_timeout=10)
    await sio.emit('on_data', 123)
    
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())