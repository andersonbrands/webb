from aiohttp.test_utils import TestClient


async def test_greeting_status_code(client: TestClient):
    resp = await client.get("/greeting")
    assert 200 == resp.status


async def test_greeting_with_no_name(client: TestClient):
    resp = await client.get("/greeting")
    assert "Hello, world!" == await resp.text()


async def test_greeting_with_name(client: TestClient):
    resp = await client.get("/greeting?name=python")
    assert "Hello, python!" in await resp.text()
