from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Response

from typing import List
from uuid import UUID

from ..database import get_async_session

from . import schemas
from ..repository.users import UserCrud
from sqlalchemy.ext.asyncio import AsyncSession

from ..utils import hash

from ..auth.oauth2 import get_current_user

router = APIRouter(
    prefix="/user",
    tags=['user']
)

@router.get("/",
            status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: {
                    "model": List[schemas.UserGet],
                    "description": "List of users"
                },
            },
            response_model=List[schemas.UserGet])
async def get_users(session: AsyncSession = Depends(get_async_session)):
    result = await UserCrud.get_all(session=session)
    return result

@router.get("/{id}",
            status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: {
                    "model": schemas.UserGet,
                    "description": "List of users"
                },
                status.HTTP_404_NOT_FOUND: {
                    "model": schemas.UserNotFound,
                    "description": "User is not found"
                }
            },
            response_model=schemas.UserGet)
async def get_user(id: UUID, session: AsyncSession = Depends(get_async_session)):
    result = await UserCrud.get_by_id(session=session, id=id)
    return result

@router.patch("/{id}",
              status_code=status.HTTP_200_OK,
              responses={
                status.HTTP_200_OK: {
                    "model": schemas.UserUpdated,
                    "description": "List of users"
                },
                status.HTTP_404_NOT_FOUND: {
                    "model": schemas.UserNotFound,
                    "description": "User is not found"
                }  
              },
              response_model=schemas.UserUpdated,
              dependencies=[Depends(get_current_user)])
async def update_user(id: UUID, updated_user: schemas.UserBase, session: AsyncSession = Depends(get_async_session)):
    await UserCrud.update_by_id(session=session, id=id, updated_user=updated_user)
    return schemas.UserUpdated()

@router.delete("/{id}",
              status_code=status.HTTP_200_OK,
              responses={
                status.HTTP_204_NO_CONTENT: {
                    "description": "User is deleted"
                },
                status.HTTP_404_NOT_FOUND: {
                    "model": schemas.UserNotFound,
                    "description": "User is not found"
                }  
              },
              response_model=schemas.UserDeleted,
              dependencies=[Depends(get_current_user)])
async def delete_user(id: UUID, session: AsyncSession = Depends(get_async_session)):
    await UserCrud.delete_by_id(session=session, id=id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
