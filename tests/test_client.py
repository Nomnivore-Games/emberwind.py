import os
import pytest

from dotenv import load_dotenv
from emberwind import Client

pytestmark = pytest.mark.anyio

load_dotenv()
EMBERWIND_API_KEY = os.getenv("EMBERWIND_API_KEY")

URL = "https://emberwind.gflcdevelopment.com/emberwind-web/api/v1/web"


async def test_create_client_without_url():
    async with Client(key=EMBERWIND_API_KEY) as client:
        assert client.url == "https://emberwindgame.com/emberwind-web/api/v1/web"






async def test_create_client_with_url():
    async with Client(key="", url=URL) as client:
        assert client.url == URL


async def test_get_all_news():
    async with Client(key=EMBERWIND_API_KEY, url=URL) as client:
        news = await client.get_all_news()
        assert news is not None


async def test_get_article():
    async with Client(key=EMBERWIND_API_KEY, url=URL) as client:
        article = await client.get_article(slug="special-dlc-dyson-the-goodest-boy")
        assert article is not None


async def test_get_article_from_article():
    async with Client(key=EMBERWIND_API_KEY, url=URL) as client:
        article = await client.get_article(
            article=(await client.get_all_news()).articles[0]
        )
        assert article is not None


async def test_get_all_faq():
    async with Client(key=EMBERWIND_API_KEY, url=URL) as client:
        faq = await client.get_all_faq()
        assert faq is not None


async def test_get_question():
    async with Client(key=EMBERWIND_API_KEY, url=URL) as client:
        question = await client.get_question(slug="i-hit-a-foe-with-a-sustain-action")
        assert question is not None


async def test_get_top_faqs():
    async with Client(key=EMBERWIND_API_KEY, url=URL) as client:
        faq = await client.get_top_faqs()
        assert faq is not None


async def test_get_all_topics():
    async with Client(key=EMBERWIND_API_KEY, url=URL) as client:
        topics = await client.get_all_topics()
        assert topics is not None


async def test_get_topic():
    async with Client(key=EMBERWIND_API_KEY, url=URL) as client:
        topic = await client.get_topic(slug="general")
        assert topic is not None


async def test_get_topic_navigation():
    async with Client(key=EMBERWIND_API_KEY, url=URL) as client:
        topic = await client.get_topic_navigation()
        assert topic is not None
