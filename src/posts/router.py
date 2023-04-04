from fastapi import APIRouter
from fastapi import status
from fastapi import Response
from fastapi import Depends

from typing import List

from crud.posts import PostsCrud

from posts import schemas
from posts.schemas import *

from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from database import get_async_session

router = APIRouter(
    prefix="/posts",
    tags=['posts']
)


@router.post('/create', 
             status_code=status.HTTP_201_CREATED,
             responses={
                 status.HTTP_201_CREATED: {
                     "model": PostCreated,
                     "description": "User post is created"
                 }
             })
async def create_post(post: schemas.PostBase, session: AsyncSession = Depends(get_async_session)):
    await PostsCrud.create(session=session, post=post)
    return PostCreated()

@router.get('/', 
            status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: {
                    "model": List[schemas.PostAll],
                    "description": "List of posts given to user"
                }
            },
            response_model=List[schemas.PostAll])
async def get_posts(session: AsyncSession = Depends(get_async_session)):
    result = await PostsCrud.get_all(session=session)
    return result

@router.get('/{id}', 
            status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: {
                    "model": schemas.PostAll,
                    "description": "User post is given to user"
                },
                status.HTTP_404_NOT_FOUND: {
                    "description": "User post is not found"
                }
            },
            response_model=schemas.PostAll)
async def get_post(id: UUID, session: AsyncSession = Depends(get_async_session)):
    result = await PostsCrud.get_by_id(session=session, id=id)
    return result

@router.patch('/{id}', 
              status_code=status.HTTP_202_ACCEPTED,
              responses={
                status.HTTP_202_ACCEPTED: {
                    "model": PostUpdated,
                    "description": "User post is updated"
                },
                status.HTTP_404_NOT_FOUND: {
                    "model": PostNotFound,
                    "description": "User post is not found"
                }
             })
async def update_post(id: UUID, post: schemas.PostBase, session: AsyncSession = Depends(get_async_session)):
    result = await PostsCrud.update_by_id(session=session, id=id, new_post=post)
    return result

@router.delete('/{id}', 
               status_code=status.HTTP_204_NO_CONTENT,
               responses={
                   status.HTTP_204_NO_CONTENT: {
                       "description": "User deleted"
                   },
                   status.HTTP_404_NOT_FOUND: {
                       "model": PostNotFound,
                       "description": "User post is not found"
                    }
               })
async def delete_post(id: UUID, session: AsyncSession = Depends(get_async_session)):
    result = await PostsCrud.delete_by_id(session=session, id=id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)