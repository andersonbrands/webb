import pytest
from aiohttp.test_utils import TestClient

from web_app import get_web_app


@pytest.fixture
async def client(aiohttp_client) -> TestClient:
    app = get_web_app()
    client = await aiohttp_client(app)
    return client
