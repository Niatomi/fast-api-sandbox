from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Response

from typing import List

from users import schemas
from database import get_async_session

from sqlalchemy.ext.asyncio import AsyncSession

from crud.users import UserCrud

from uuid import UUID

router = APIRouter(
    prefix="/user",
    tags=['user']
)


@router.post("/create",
             status_code=status.HTTP_201_CREATED,
             responses={
                 status.HTTP_201_CREATED: {
                     "model": schemas.UserCreated,
                     "description": "User created"
                 },
                 status.HTTP_400_BAD_REQUEST: {
                     "model": schemas.UserAlreadyExists,
                     "description": "User already exists"
                 }
             },
             response_model=schemas.UserCreated)
async def create_user(new_user: schemas.UserCreate, session: AsyncSession = Depends(get_async_session)):
    await UserCrud.create(session=session, user=new_user)
    return schemas.UserCreated()

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
              response_model=schemas.UserUpdated)
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
              response_model=schemas.UserDeleted)
async def delete_user(id: UUID, session: AsyncSession = Depends(get_async_session)):
    await UserCrud.delete_by_id(session=session, id=id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
