from fastapi import status
from fastapi.responses import JSONResponse
from . import schemas as user_schemas
from fastapi import Request

class UserNotFoundException(Exception):
    pass

class UserAlreadyExistsException(Exception):
    pass

def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    content = user_schemas.UserNotFound().dict()
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=content)

def user_already_exists_exception_handler(request: Request, exc: UserAlreadyExistsException):
    content = user_schemas.UserAlreadyExists().dict()
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=content)