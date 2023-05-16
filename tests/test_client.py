import pytest
import asyncio
import trio

from emberwind import Client

pytestmark = pytest.mark.anyio


async def test_client_create():
    client = Client(
        key="",
        email="",
        password="",
    )

    assert client.key == ""
    assert client.email == ""
    assert client.password == ""
