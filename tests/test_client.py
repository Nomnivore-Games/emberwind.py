import os
import pytest

from dotenv import load_dotenv
from emberwind import Client

pytestmark = pytest.mark.anyio

load_dotenv()
EMBERWIND_API_KEY = os.getenv("EMBERWIND_API_KEY")


async def test_client_create():
    async with Client(key="") as client:
        assert client.key == ""
        assert client.email == ""
        assert client.password == ""


async def test_client_get_all_news():
    async with Client(key=EMBERWIND_API_KEY) as client:
        news = await client.get_all_news()
        assert news is not None


async def test_client_get_article():
    async with Client(key=EMBERWIND_API_KEY) as client:
        article = await client.get_article(slug="special-dlc-dyson-the-goodest-boy")
        assert article is not None
