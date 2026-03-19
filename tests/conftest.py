import pytest
from crya.testing import TestClient

from bootstrap import app


@pytest.fixture
async def client():
    async with TestClient(app) as client:
        yield client
