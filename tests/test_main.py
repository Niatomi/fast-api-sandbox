import pytest
from httpx import AsyncClient

from fastapi.testclient import TestClient

from src.__main__ import app


@pytest.mark.anyio
async def test_ping():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/ping")
    assert response.status_code == 200
    assert response.text == 'pong'
    
