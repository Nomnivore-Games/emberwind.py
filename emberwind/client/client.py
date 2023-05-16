from asks import Session

from emberwind.client.content import NewsController
from emberwind.models.emberwind.article import Article
from emberwind.models.emberwind.enums import Order, Sorting, Category
from emberwind.models.emberwind.news import News


class Client:
    def __init__(self, key: str, email: str = "", password: str = ""):
        """Initialize the client with the key, email, and password.
        :param key: The API key for the client.
        :param email: The email for the client.
        :param password: The password for the client."""

        self.key = key
        self.email = email
        self.password = password

    async def __aenter__(self):
        self.session = Session()
        self.session.headers.update({"Emberwind-Api-Key": self.key})
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

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
            page=page,
            size=size,
            order_by=order_by,
            sorting=sorting,
            categories=categories,
            title=title,
        )

        return await news

    async def get_article(self, slug: str = None, article: Article = None) -> Article:
        article = NewsController.get_article(self.session, slug=slug, article=article)

        return await article
