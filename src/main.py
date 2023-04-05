import uvicorn

from fastapi import FastAPI
from fastapi import Depends
from fastapi.openapi.docs import get_swagger_ui_html
import exceptions    
from fastapi.middleware.cors import CORSMiddleware

from posts.router import router as posts_router
from users.router import router as users_router
from auth.router import router as auth_router

from auth.oauth2 import get_current_user

app = FastAPI()

app.include_router(router=auth_router)
app.include_router(router=posts_router, dependencies=[Depends(get_current_user)])
app.include_router(router=users_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

exceptions.include_app(app) 

if __name__ == "__main__":
    uvicorn.run(app="main:app", host='0.0.0.0', port=8000, reload=True)