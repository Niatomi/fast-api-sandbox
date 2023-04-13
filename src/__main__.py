import uvicorn

from fastapi import FastAPI
from fastapi import status
from fastapi import Response
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

base_responses = {
    400: {"description": "Bad Request"},
    401: {"description": "Unauthorized"},
    404: {"description": "Not Found"},
    422: {"description": "Validation Error"},
    500: {"description": "Internal Server Error"}
}

general_responses = {
    **base_responses,
    200: {
        "content": {
            "application/json": {
                "example": {"message": "success"}
            }
        },
    }
}

@app.get("/inc", responses=general_responses)
def inc(x: int):
    return x + 1

@app.get("/ping", include_in_schema=False)
async def home():
    return Response(status_code=status.HTTP_200_OK,
                    content="pong")

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