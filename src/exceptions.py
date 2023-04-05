from fastapi import FastAPI, HTTPException, status
from fastapi import status
from fastapi import Request
from fastapi import Response

from fastapi.responses import JSONResponse

from posts import schemas as posts_schemas
from users import schemas as user_schemas
from auth.schemas import WrongCredentials


class PostNotFoundException(Exception):
    pass

class UserNotFoundException(Exception):
    pass

class UserAlreadyExistsException(Exception):
    pass

class WrongCredentialsException(Exception):
    pass

class NotAllowedException(Exception):
    pass

def post_not_found_exception_handler(request: Request, exc: PostNotFoundException):
    content = posts_schemas.PostNotFound().dict()
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=content)

def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    content = user_schemas.UserNotFound().dict()
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=content)

def user_already_exists_exception_handler(request: Request, exc: UserAlreadyExistsException):
    content = user_schemas.UserAlreadyExists().dict()
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=content)

def wrong_credentials_handler(request: Request, exc: WrongCredentialsException):
    content = WrongCredentials().dict()
    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content=content, headers={"WWW-Authenticate": "Bearer"})

def not_allowed_handler(request: Request, exc: NotAllowedException):
    content = posts_schemas.PostChangeNotAllowed().dict()
    return JSONResponse(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, content=content)

def include_app(app: FastAPI):
	app.add_exception_handler(PostNotFoundException, post_not_found_exception_handler)
	app.add_exception_handler(UserAlreadyExistsException, user_already_exists_exception_handler)
	app.add_exception_handler(UserNotFoundException, user_not_found_exception_handler)
	app.add_exception_handler(WrongCredentialsException, wrong_credentials_handler)
	app.add_exception_handler(NotAllowedException, not_allowed_handler)