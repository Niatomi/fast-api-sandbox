from posts import schemas
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi import Request

class PostNotFoundException(Exception):
    pass

def post_not_found_exception_handler(request: Request, exc: PostNotFoundException):
    content = schemas.PostNotFound().dict()
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=content)

class NotAllowedException(Exception):
    pass

def not_allowed_handler(request: Request, exc: NotAllowedException):
    content = schemas.posts_schemas.PostChangeNotAllowed().dict()
    return JSONResponse(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, content=content)