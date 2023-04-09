import pytest

from src.__main__ import func


def test_inc():
    assert func(3) == 4
    assert func(5) == 6
    assert func(7) == 8
