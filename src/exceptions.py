from fastapi import FastAPI, HTTPException, status
from fastapi import HTTPException
from fastapi import status
from fastapi import Request
from fastapi import Response

class PostNotFoundException(Exception):
    pass


def perfect_exception_handler(request: Request, exc: HTTPException):
    return Response(status_code=status.HTTP_404_NOT_FOUND, content="Post not found ")

def include_app(app):
	app.add_exception_handler(PostNotFoundException, perfect_exception_handler)