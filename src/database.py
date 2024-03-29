from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from typing import AsyncGenerator

import configparser

import os

_config = configparser.ConfigParser()
_config.read("config.ini")


from .config import config

from sqlalchemy.ext.asyncio import AsyncSession

DATABASE_URL = f"postgresql+asyncpg://{config.db_user}:{config.db_pass}@{config.db_host}:{config.db_port}/{config.db_name}"

print(DATABASE_URL)

engine = create_async_engine(DATABASE_URL, echo=_config.getboolean('SQLAlchemy', 'ddl_show'))

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session