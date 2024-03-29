from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Form

from ..database import get_async_session
from .schemas import *
from sqlalchemy.ext.asyncio import AsyncSession
from ..repository.users import UserCrud

from ..utils import *
from .exceptions import WrongCredentialsException
from ..users.exceptions import UserAlreadyExistsException
from .oauth2 import (
    create_access_token
)
from ..users.schemas import (
    UserCreate,
    UserAlreadyExists
)
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    tags=["authentication"]
)

from pydantic.dataclasses import dataclass


@dataclass
class AdditionalUserDataForm:
    email: str = Form(None)

@router.post('/sign_in',
             responses={
                 status.HTTP_400_BAD_REQUEST: {
                     "model": WrongCredentials,
                     "description": "User credentials is invalid"
                 },
                 status.HTTP_200_OK: {
                     "model": UserToken,
                     "description": "Credentials is valid successfully logged in"
                 }
             },
             response_model=UserToken)
async def sign_in(user_credentials: OAuth2PasswordRequestForm = Depends(), 
                  session: AsyncSession = Depends(get_async_session), 
                  additional_info: AdditionalUserDataForm = Depends()):
    print(additional_info.email)
    user_from_db = await UserCrud.get_by_email(session=session, email=user_credentials.username)
    if not verify(user_credentials.password, user_from_db.password):
        raise WrongCredentialsException
    
    user_token = UserToken()
    user_token.access_token = create_access_token({
        "user_id": str(user_from_db.id)})
    return user_token.dict()

@router.post('/sign_up',
             responses={
                 status.HTTP_400_BAD_REQUEST: {
                     "model": UserAlreadyExists,
                     "description": "User already exists"
                 },
                 status.HTTP_200_OK: {
                     "model": UserToken,
                     "description": "Credentials is valid successfully logged in"
                 }
             },
             response_model=UserToken)
async def sign_up(sign_up_user: UserCreate, 
                  session: AsyncSession = Depends(get_async_session)):
    await UserCrud.create(session=session, user=sign_up_user)
    user_from_db = await UserCrud.get_by_email(session=session, email=sign_up_user.email)
    
    user_token = UserToken()
    user_token.access_token = create_access_token({
        "user_id": str(user_from_db.id)})
    return user_token.dict()