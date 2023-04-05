from fastapi import Depends
from fastapi import status
from exceptions import WrongCredentialsException

from fastapi.security import OAuth2PasswordBearer

from auth import schemas
from jose import JWTError, jwt
from datetime import (
    datetime,
    timedelta    
)

from models import User

from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

from crud.users import UserCrud
from uuid import UUID

from config import SECRET
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='sign_in')

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        id: str = payload.get('user_id')
        if id is None:
            raise credentials_exception
        token_data = schemas.UserToken()
        token_data.access_token = id
    except JWTError as e:
        raise credentials_exception
    return token_data
    
async def get_current_user(token: str = Depends(oauth2_scheme), session: AsyncSession = Depends(get_async_session)):
    credentials_exception = WrongCredentialsException
    access_token = verify_access_token(token, credentials_exception)
    user = await UserCrud.get_by_id(session=session, id=UUID(access_token.access_token))
    return user