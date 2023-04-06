from fastapi import FastAPI
from fastapi import status
from fastapi import Request

from fastapi.responses import JSONResponse

from posts import schemas as posts_schemas
from users import schemas as user_schemas
from auth.schemas import WrongCredentials

from votes import exceptions as votes_exceptions
from users import exceptions as user_exceptions
from posts import exceptions as posts_exceptions
from auth import exceptions as auth_exceptions

def include_app(app: FastAPI):
    app.add_exception_handler(posts_exceptions.PostNotFoundException, posts_exceptions.post_not_found_exception_handler)
    app.add_exception_handler(user_exceptions.UserAlreadyExistsException, user_exceptions.user_already_exists_exception_handler)
    app.add_exception_handler(user_exceptions.UserNotFoundException, user_exceptions.user_not_found_exception_handler)
    app.add_exception_handler(auth_exceptions.WrongCredentialsException, auth_exceptions.wrong_credentials_handler)
    app.add_exception_handler(posts_exceptions.NotAllowedException, posts_exceptions.not_allowed_handler)
    app.add_exception_handler(votes_exceptions.VoteException, votes_exceptions.vote_exception_handler)