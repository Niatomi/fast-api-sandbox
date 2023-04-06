from fastapi import Request
from fastapi import status
from votes.schemas import VoteExceptionResponse
from fastapi.responses import JSONResponse

class VoteException(Exception):
    pass

def vote_exception_handler(request: Request, exc: VoteException):
    content = VoteExceptionResponse().dict()
    return JSONResponse(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, content=content)