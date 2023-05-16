from asks import Session
from emberwind.models.emberwind.news import News
from emberwind.models.emberwind.article import Article
from emberwind.models.emberwind.enums import Order, Sorting, Category


class NewsController:
    @staticmethod
    async def get_all_news(
        session: Session,
        page: int = 0,
        size: int = 20,
        order_by: Order = Order.TITLE,
        sorting: Sorting = Sorting.DESCENDING,
        categories: list[Category] = None,
        title: str = "",
    ) -> News:
        if categories is None:
            categories = []

        response = await session.get(
            "http://emberwind.gflcdevelopment.com/emberwind-web/api/v1/web/content/news",
            params={
                "page": page,
                "size": size,
                "orderBy": order_by.value,
                "ordering": sorting.value,
                "categories": [c.value for c in categories],
                "title": title,
            },
        )

        return News.from_json(response.json())

    @staticmethod
    async def _get_article_from_slug(session: Session, slug: str) -> Article:
        response = await session.get(
            "http://emberwind.gflcdevelopment.com/emberwind-web/api/v1/web/content/news/"
            + slug,
        )

        return Article.from_json(response.json())

    @staticmethod
    async def get_article(
        session: Session, slug: str = None, article: Article = None
    ) -> Article:
        if slug:
            return await NewsController._get_article_from_slug(session, slug)

        if article:
            return await NewsController._get_article_from_slug(session, article.slug)
