from sqlalchemy.ext.asyncio import AsyncSession

from schemas import Post as SchemasPost

from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import delete

from models import Post

from exceptions import PostNotFoundException

from uuid import UUID

class PostsCrud():
    
    @staticmethod
    async def create(session: AsyncSession, post: SchemasPost):
        input_data = post.dict()
        if input_data.get('id') is not None:
            input_data.pop('id')
        new_data = Post(**input_data)
        session.add(new_data)
        await session.commit()
    
    @staticmethod
    async def get_all(session: AsyncSession):
        statement = select(Post).order_by(Post.id)
        result = await session.execute(statement)
        return result.scalars().all()
        
    
    @staticmethod
    async def get_by_id(session: AsyncSession, id: UUID):
        statement = select(Post).where(Post.id == id)
        result = await session.execute(statement)
        post = result.scalars().first()
        if post is None:
            raise PostNotFoundException()
        return post
        
    @staticmethod
    async def update_by_id(session: AsyncSession, id: UUID, new_post: SchemasPost):
        result = await PostsCrud.get_by_id(session=session, id=id)
        new_post = new_post.dict()
        new_post['id'] = id
        statement = (update(Post).
                 where(Post.id == id).
                 values(new_post)
                )
        await session.execute(statement)
        await session.commit()
        return "Data updated"
    
    @staticmethod
    async def delete_by_id(session: AsyncSession, id: UUID):
        result = await PostsCrud.get_by_id(session=session, id=id)
        statement = delete(Post).where(Post.id == id)
        result = await session.execute(statement)
        await session.commit()
        return "Data deleted"