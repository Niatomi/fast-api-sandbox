import pytest
import asyncio

from src.__main__ import app
from src.database import get_async_session
from src.users import schemas as user_schemas

from fastapi.testclient import TestClient
from uuid import uuid4

from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from typing import AsyncGenerator

from .test_config import test_config

from src.models import Base

DATABASE_URL = f"postgresql+asyncpg://{test_config.db_user}:{test_config.db_pass}@{test_config.db_host}:{test_config.db_port}/{test_config.db_name}"

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
    

async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()

async def drop_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()

import pytest_asyncio


@pytest.fixture
async def client():
    init_models()
    yield TestClient(app)
    drop_models()
    
@pytest.mark.asyncio
async def test_create_user(client):
    json = user_schemas.UserCreate(name="test", 
                                   email="test@example.com", 
                                   password="test").dict()
    response = client.post('/sign_up', json=json)
    assert response.status_code == 200
    
    response = client.post('/sign_up', json=json)
    assert response.status_code == 400
    assert response.json().get('message') == "USER_IS_ALREADY_EXISTS"
    