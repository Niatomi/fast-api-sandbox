from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from database import get_async_session
from auth.schemas import *
from sqlalchemy.ext.asyncio import AsyncSession
from crud.users import UserCrud

from utils import *
from exceptions import WrongCredentialsException
from auth.oauth2 import (
    create_access_token
)

from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    tags=["Authentication"]
)

@router.post('/login',
             responses={
                 status.HTTP_400_BAD_REQUEST: {
                     "model": WrongCredentials,
                     "description": "User credentials is invalid"
                 },
                 status.HTTP_200_OK: {
                     "model": UserToken,
                     "description": "Credentials is valid successfully logged in"
                 }
             })
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_async_session)):
    user_from_db = await UserCrud.get_by_email(session=session, email=user_credentials.username)
    print(user_from_db.password)
    if not verify(user_credentials.password, user_from_db.password):
        raise WrongCredentialsException
    
    user_token = UserToken()
    user_token.token = create_access_token({
        "user_id": str(user_from_db.id), 
        "token_type": "bearer"})
    return user_token
        