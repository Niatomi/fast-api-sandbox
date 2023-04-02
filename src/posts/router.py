from fastapi import APIRouter
from fastapi import status
from fastapi import Response
from fastapi import Depends

from crud.posts import PostsCrud
from schemas import Post as SchemasPost
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from database import get_async_session

router = APIRouter(
    prefix="/posts"
)

@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_post(post: SchemasPost, session: AsyncSession = Depends(get_async_session)):
    PostsCrud.create(session=session, post=post)
    return 'Data saved'

@router.get('/', status_code=status.HTTP_200_OK)
async def get_posts(session: AsyncSession = Depends(get_async_session)):
    result = await PostsCrud.get_all(session=session)
    return result

@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_posts(id: UUID, session: AsyncSession = Depends(get_async_session)):
    result = await PostsCrud.get_by_id(session=session, id=id)
    print(result)
    return result

@router.patch('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_post(id: UUID, post: SchemasPost, session: AsyncSession = Depends(get_async_session)):
    result = await PostsCrud.update_by_id(session=session, id=id, new_post=post)
    return result

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: UUID, session: AsyncSession = Depends(get_async_session)):
    result = await PostsCrud.delete_by_id(session=session, id=id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)