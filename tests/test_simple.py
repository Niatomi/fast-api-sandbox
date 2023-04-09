import pytest
from src.main import app


async def test_inc():
    assert app.add(3) == 4


def func_exc():
    raise Exception


def test_func_exc():
    with pytest.raises(Exception):
        func_exc()