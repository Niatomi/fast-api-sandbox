from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from votes import schemas

from sqlalchemy import select
from sqlalchemy import delete

from models import Votes

class VoteCrud():
    
    @staticmethod
    async def create(session: AsyncSession, vote: schemas.Vote):
        session.add(Votes(**vote.dict()))
        await session.commit()
    
    @staticmethod
    async def get_by_body(session: AsyncSession, vote: schemas.Vote):
        query = select(Votes).where(Votes.user_id == vote.user_id and Votes.post_id == vote.post_id)
        result = await session.execute(query)
        result = result.scalars().first()
        return result
        
    
    @staticmethod
    async def delete(session: AsyncSession, vote: schemas.Vote):
        statement = delete(Votes).where(Votes.user_id == vote.user_id and Votes.post_id == vote.post_id)
        await session.execute(statement)
        await session.commit()
        pass
    
    
    
    