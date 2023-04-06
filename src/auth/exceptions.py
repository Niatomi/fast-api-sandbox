from auth.schemas import WrongCredentials
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi import Request

class WrongCredentialsException(Exception):
    pass

def wrong_credentials_handler(request: Request, exc: WrongCredentialsException):
    content = WrongCredentials().dict()
    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content=content, headers={"WWW-Authenticate": "Bearer"})