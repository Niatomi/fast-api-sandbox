from sqlalchemy.ext.asyncio import AsyncSession

from users.schemas import User as UserSchema

class UserCrud():
    
    @staticmethod
    async def create(session: AsyncSession, user: UserSchema):
        pass
    
    @staticmethod
    async def get_all(session: AsyncSession):
        pass 
    
    @staticmethod
    async def get_by_id(session: AsyncSession):
        pass 
    
    @staticmethod
    async def update_by_id(session: AsyncSession):
        pass 
    
    @staticmethod
    async def delete_by_id(session: AsyncSession):
        pass 
    