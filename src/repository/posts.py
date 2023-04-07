from sqlalchemy.ext.asyncio import AsyncSession

from posts import schemas

from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy import func

from sqlalchemy.orm import joinedload
from sqlalchemy.orm import load_only

from models import Post
from models import Votes
from models import User

from posts.exceptions import PostNotFoundException

from sqlalchemy import inspect

from uuid import UUID

class PostsCrud():
    
    @staticmethod
    async def create(session: AsyncSession, post: schemas.PostBase):
        input_data = post.dict()
        if input_data.get('id') is not None:
            input_data.pop('id')
        new_data = Post(**input_data)
        session.add(new_data)
        await session.commit()
    
    @staticmethod
    async def get_all(session: AsyncSession):
        # statement = select(Post).order_by(Post.id).join(Votes, Votes.post_id == Post.id, isouter=True).group_by(Post.id)
        statement = select(func.count(Votes.user_id).label('votes')).join(Votes, Votes.post_id == Post.id, isouter=True).group_by(Post.id)
        
        stmt = (
            select(Post, User, func.count(Votes.user_id).label('votes'))
            .join(Votes, Votes.post_id == Post.id, isouter=True)
            .join(User, User.id == Post.owner_id, isouter=True)
            .group_by(Post.id, User.id)
            
        )
        result = await session.execute(stmt)
        result = result.fetchall()
        result = [el._asdict() for el in result]
        return result
    
    @staticmethod
    async def get_pagination(session: AsyncSession, 
                             items_size: int, 
                             page: int):
        page = page - 1
        stmt = (
            select(Post, User, func.count(Votes.user_id).label('votes'))
            .join(Votes, Votes.post_id == Post.id, isouter=True)
            .join(User, User.id == Post.owner_id, isouter=True)
            .group_by(Post.id, User.id)
            .offset(page*items_size)
            .limit(items_size)
        )
        result = await session.execute(stmt)
        result = result.fetchall()
        result = [el._asdict() for el in result]
        return result
    
    @staticmethod
    async def get_by_id(session: AsyncSession, id: UUID):
        stmt = (
            select(Post, User, func.count(Votes.user_id).label('votes'))
            .join(Votes, Votes.post_id == Post.id, isouter=True)
            .join(User, User.id == Post.owner_id, isouter=True)
            .group_by(Post.id, User.id)
            .where(Post.id == id)   
        )
        result = await session.execute(stmt)
        result = result.first()
        if result is None:
            raise PostNotFoundException()
        return result._asdict()
        
    @staticmethod
    async def update_by_id(session: AsyncSession, id: UUID, new_post: schemas.PostBase):
        await PostsCrud.get_by_id(session=session, id=id)
        new_post = new_post.dict()
        new_post['id'] = id
        statement = (update(Post).
                 where(Post.id == id).
                 values(new_post)
                )
        await session.execute(statement)
        await session.commit()
        await session.refresh(new_post)
        return schemas.PostUpdated()
    
    @staticmethod
    async def delete_by_id(session: AsyncSession, id: UUID):
        await PostsCrud.get_by_id(session=session, id=id)
        statement = delete(Post).where(Post.id == id)
        
        await session.execute(statement)
        await session.commit()
        return schemas.PostDeleted()
    