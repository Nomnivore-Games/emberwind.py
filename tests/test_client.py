import os
import pytest

from dotenv import load_dotenv
from emberwind import Client

pytestmark = pytest.mark.anyio

load_dotenv()
EMBERWIND_API_KEY = os.getenv("EMBERWIND_API_KEY")
EMBERWIND_EMAIL = os.getenv("EMBERWIND_TEST_EMAIL")
EMBERWIND_PASSWORD = os.getenv("EMBERWIND_TEST_PASSWORD")

URL = "https://emberwind.gflcdevelopment.com/emberwind-web/api/v1/web"


async def test_create_client_without_url():
    client = Client(key=EMBERWIND_API_KEY)
    assert client.url == "https://emberwindgame.com/emberwind-web/api/v1/web"
    await client.close()


async def test_create_client_with_url():
    client = Client(key="", url=URL)
    assert client.url == URL
    await client.close()


async def test_get_all_news():
    client = Client(key=EMBERWIND_API_KEY, url=URL)
    news = await client.get_all_news()
    assert news is not None
    await client.close()


async def test_get_article():
    client = Client(key=EMBERWIND_API_KEY, url=URL)
    article = await client.get_article(slug="special-dlc-dyson-the-goodest-boy")
    assert article is not None
    await client.close()


async def test_get_article_from_article():
    client = Client(key=EMBERWIND_API_KEY, url=URL)
    article = await client.get_article(
        article=(await client.get_all_news()).articles[0]
    )
    assert article is not None
    await client.close()


async def test_get_all_faq():
    client = Client(key=EMBERWIND_API_KEY, url=URL)
    faq = await client.get_all_faq()
    assert faq is not None
    await client.close()


async def test_get_question():
    client = Client(key=EMBERWIND_API_KEY, url=URL)
    question = await client.get_question(slug="i-hit-a-foe-with-a-sustain-action")
    assert question is not None
    await client.close()


async def test_get_top_faqs():
    client = Client(key=EMBERWIND_API_KEY, url=URL)
    faq = await client.get_top_faqs()
    assert faq is not None
    await client.close()


async def test_get_all_topics():
    client = Client(key=EMBERWIND_API_KEY, url=URL)
    topics = await client.get_all_topics()
    assert topics is not None
    await client.close()


async def test_get_topic():
    client = Client(key=EMBERWIND_API_KEY, url=URL)
    topic = await client.get_topic(slug="general")
    assert topic is not None
    await client.close()


async def test_get_topic_navigation():
    client = Client(key=EMBERWIND_API_KEY, url=URL)
    topic = await client.get_topic_navigation()
    assert topic is not None
    await client.close()


async def test_login():
    client = Client(key=EMBERWIND_API_KEY, url=URL)
    login = await client.login(email=EMBERWIND_EMAIL, password=EMBERWIND_PASSWORD)
    assert login is not None
    assert client.user is not None
    await client.close()


async def test_logout():
    client = Client(key=EMBERWIND_API_KEY, url=URL)
    await client.logout()
    assert client.user is None
    await client.close()
