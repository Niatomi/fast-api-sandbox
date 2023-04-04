from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy import delete
from sqlalchemy import update

from pydantic import EmailStr

from users import schemas

from exceptions import (
    UserNotFoundException, 
    UserAlreadyExistsException
)

from models import User

from uuid import UUID


class UserCrud():
    
    @staticmethod
    async def get_by_email(session: AsyncSession, email: EmailStr):
        query = select(User).where(User.email == email)
        result = await session.execute(query)
        return result.scalars().first()
    
    @staticmethod
    async def create(session: AsyncSession, user: schemas.UserCreate):
        result = await UserCrud.get_by_email(session=session, email=user.email)
        if result is not None:
            raise UserAlreadyExistsException
        session.add(User(**user.dict()))
        await session.commit()
    
    @staticmethod
    async def get_all(session: AsyncSession):
        statement = select(User).order_by(User.id)
        result = await session.execute(statement)
        return result.scalars().all()
    
    @staticmethod
    async def get_by_id(session: AsyncSession, id: UUID):
        statement = select(User).where(User.id == id)
        result = await session.execute(statement)
        user = result.scalars().first()
        if user is None:
            raise UserNotFoundException
        return user
        
    
    @staticmethod
    async def update_by_id(session: AsyncSession, id:UUID, updated_user: schemas.UserBase):
        result = await UserCrud.get_by_id(session=session, id=id)
        updated_user = updated_user.dict()
        updated_user['id'] = id
        statement = update(User).where(User.id == id).values(updated_user)
        await session.execute(statement)
        await session.commit()
        return schemas.UserUpdated()
    
    @staticmethod
    async def delete_by_id(session: AsyncSession, id: UUID):
        result = await UserCrud.get_by_id(session=session, id=id)
        statement = delete(User).where(User.id == id)
        result = await session.execute(statement)
        await session.commit()
        return schemas.UserDeleted()
    