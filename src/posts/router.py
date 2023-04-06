from fastapi import APIRouter
from fastapi import status
from fastapi import Response
from fastapi import Depends

from typing import List

from repository.posts import PostsCrud

from posts import schemas
from posts.schemas import *

from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from database import get_async_session

from auth.oauth2 import get_current_user

from posts.utils import check_user_own

from models import User

from uuid import uuid4

router = APIRouter(
    prefix="/posts",
    tags=['posts'],
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "User is not logged in"
        }
    }
)

@router.post('/create', 
             status_code=status.HTTP_201_CREATED,
             responses={
                 status.HTTP_201_CREATED: {
                     "model": PostCreated,
                     "description": "User post is created"
                 }
             })
async def create_post(post: schemas.PostBase, 
                      session: AsyncSession = Depends(get_async_session),
                      user: User = Depends(get_current_user)):
    new_post = PostCreate(**post.dict(), id=uuid4(), owner_id=user.id)
    new_post.created_at = datetime.now()
    await PostsCrud.create(session=session, post=new_post)
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

@router.get('/pages', 
            status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: {
                    "model": List[schemas.PostAll],
                    "description": "List of posts given to user"
                }
            },
            response_model=List[schemas.PostAll])
async def get_posts(session: AsyncSession = Depends(get_async_session),
                    items_size: int = 10,
                    page: int = 1):
    result = await PostsCrud.get_pagination(
        session=session,
        items_size=items_size,
        page=page)
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
                },
                status.HTTP_405_METHOD_NOT_ALLOWED: {
                    "model": PostChangeNotAllowed,
                    "description": "User doesn't have an access for current post"
                }
              },
              dependencies=[Depends(check_user_own)])
async def update_post(id: UUID, post: schemas.PostBase, 
                      session: AsyncSession = Depends(get_async_session)):
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
                    },
                    status.HTTP_405_METHOD_NOT_ALLOWED: {
                       "model": PostChangeNotAllowed,
                       "description": "User doesn't have an access for current post"
                    }
               },
               dependencies=[Depends(check_user_own)])
async def delete_post(id: UUID, 
                      session: AsyncSession = Depends(get_async_session),
                      user: User = Depends(get_current_user)):
    result = await PostsCrud.delete_by_id(session=session, id=id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)