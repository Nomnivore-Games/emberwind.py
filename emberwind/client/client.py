from asks import Session

from emberwind.client.content import NewsController, FAQController
from emberwind.models.emberwind.enums import Order, Sorting, Category
from emberwind.models.emberwind.faq import FAQ, Question, Topic
from emberwind.models.emberwind.news import Article, News


class Client:
    def __init__(self, key: str, email: str = "", password: str = "", url: str = ""):
        """Initialize the client with the key, email, and password.
        :param key: The API key for the client.
        :param email: The email for the client.
        :param password: The password for the client."""

        self.key = key
        self.email = email
        self.password = password

        if not url:
            self.url = "https://emberwindgame.com/emberwind-web/api/v1/web"
        else:
            self.url = url

    async def __aenter__(self):
        self.session = Session()
        self.session.headers.update({"Emberwind-Api-Key": self.key})
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    async def get_all_faq(
        self, keyword: str = "", page: int = 0, size: int = 10
    ) -> FAQ:
        faq = FAQController.get_all_faqs(
            self.session, self.url, keyword=keyword, page=page, size=size
        )

        return await faq

    async def get_question(self, slug: str = None) -> Question:
        question = FAQController.get_question(
            self.session,
            self.url,
            slug=slug,
        )

        return await question

    async def get_top_faqs(self) -> list[Question]:
        faq = FAQController.get_top_faqs(
            self.session,
            self.url,
        )

        return await faq

    async def get_all_topics(
        self,
    ) -> list[Topic]:
        topics = FAQController.get_all_topics(
            self.session,
            self.url,
        )

        return await topics

    async def get_topic(self, slug: str = None) -> Topic:
        topic = FAQController.get_topic(
            self.session,
            self.url,
            slug=slug,
        )

        return await topic

    async def get_topic_navigation(self) -> list[Topic]:
        topic = FAQController.get_topic_navigation(
            self.session,
            self.url,
        )

        return await topic

    async def get_all_news(
        self,
        page: int = 0,
        size: int = 20,
        order_by: Order = Order.TITLE,
        sorting: Sorting = Sorting.DESCENDING,
        categories: list[Category] = None,
        title: str = "",
    ) -> News:
        news = NewsController.get_all_news(
            self.session,
            self.url,
            page=page,
            size=size,
            order_by=order_by,
            sorting=sorting,
            categories=categories,
            title=title,
        )

        return await news

    async def get_article(self, slug: str = None, article: Article = None) -> Article:
        article = NewsController.get_article(
            self.session, self.url, slug=slug, article=article
        )

        return await article
