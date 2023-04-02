from fastapi import FastAPI, HTTPException, status
from fastapi import HTTPException
from fastapi import status
from fastapi import Request
from fastapi import Response

from posts.schemas import PostNotFound
from users.schemas import UserNotFound

class PostNotFoundException(Exception):
    pass

class UserNotFoundException(Exception):
    pass


def post_not_found_exception_handler(request: Request, exc: HTTPException):
    content = PostNotFound
    return Response(status_code=status.HTTP_404_NOT_FOUND, content=content)

def user_not_found_exception_handler(request: Request, exc: HTTPException):
    content = UserNotFound
    return Response(status_code=status.HTTP_404_NOT_FOUND, content=content)


def include_app(app):
	app.add_exception_handler(PostNotFoundException, post_not_found_exception_handler)