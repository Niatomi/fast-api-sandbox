from config import DB_HOST, DB_PORT, DB_PASS, DB_USER, DB_NAME
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

from typing import AsyncGenerator

import configparser

config = configparser.ConfigParser()
config.read("../config.ini")

from sqlalchemy.ext.asyncio import AsyncSession

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?async_fallback=true"
Base = declarative_base()

engine = create_async_engine(DATABASE_URL, echo=config.getboolean('SQLAlchemy', 'ddl_show'))

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session