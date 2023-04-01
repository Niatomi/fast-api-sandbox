import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ws.ws import sio_app


app = FastAPI()
app.mount('/', app=sio_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def func():
    return 'Hello'


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)