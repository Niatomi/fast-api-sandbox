from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Response

from typing import List

from users.schemas import *
from database import get_async_session

from sqlalchemy.ext.asyncio import AsyncSession

from uuid import UUID

router = APIRouter(
    prefix="/user",
    tags=['user']
)


@router.post("/",
             status_code=status.HTTP_201_CREATED,
             responses={
                 status.HTTP_201_CREATED: {
                     "model": UserCreated,
                     "description": "User created"
                 }
             })
def create_user(new_user: User, session: AsyncSession = Depends(get_async_session)):
    # Implementation
    return UserCreated

@router.get("/",
            status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: {
                    "model": List[User],
                    "description": "List of users"
                },
            })
def get_users(id: UUID, session: AsyncSession = Depends(get_async_session)):
    # Implementation
    pass

@router.get("/{id}",
            status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: {
                    "model": User,
                    "description": "List of users"
                },
                status.HTTP_404_NOT_FOUND: {
                    "model": UserNotFound,
                    "description": "User is not found"
                }
            })
def get_user(id: UUID, session: AsyncSession = Depends(get_async_session)):
    # Implementation
    pass

@router.patch("/{id}",
              status_code=status.HTTP_200_OK,
              responses={
                status.HTTP_200_OK: {
                    "model": UserUpdated,
                    "description": "List of users"
                },
                status.HTTP_404_NOT_FOUND: {
                    "model": UserNotFound,
                    "description": "User is not found"
                }  
            })
def update_user(id: UUID, session: AsyncSession = Depends(get_async_session)):
    # Implementation
    return UserUpdated

@router.delete("/{id}",
              status_code=status.HTTP_200_OK,
              responses={
                status.HTTP_204_NO_CONTENT: {
                    "description": "User is deleted"
                },
                status.HTTP_404_NOT_FOUND: {
                    "model": UserNotFound,
                    "description": "User is not found"
                }  
            })
def delete_user(id: UUID, session: AsyncSession = Depends(get_async_session)):
    # Implementation
    return Response(status_code=status.HTTP_204_NO_CONTENT)
