import uvicorn

from fastapi import FastAPI
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware

print(__name__)

from .exceptions import include_app

from .posts.router import router as posts_router
from .users.router import router as users_router
from .auth.router import router as auth_router
from .votes.router import router as votes_router

app = FastAPI(
    title='Nia\'s social network service',
    version='1.0'
)

@app.get("/")
def func(x: int):
    return x + 1

app.include_router(router=auth_router)
app.include_router(router=posts_router)
app.include_router(router=users_router)
app.include_router(router=votes_router)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "DELETE"],
    allow_headers=["*"],
)

include_app(app) 

if __name__ == "__main__":
    uvicorn.run(app=app, host='0.0.0.0', port=8000)