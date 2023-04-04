from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from database import get_async_session
from auth.schemas import *
from sqlalchemy.ext.asyncio import AsyncSession
from crud.users import UserCrud
from utils import *
from exceptions import WrongCredentialsException

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
async def login(user_credentials: UserCredentials, session: AsyncSession = Depends(get_async_session)):
    user_from_db = await UserCrud.get_by_email(session=session, email=user_credentials.email)
    if not verify(user_credentials.password, user_from_db.password):
        raise WrongCredentialsException
    
    user_token = UserToken()
    user_token.token = "123123123"
    return user_token
        