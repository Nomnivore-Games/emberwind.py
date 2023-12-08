from asks import Session

from emberwind.models.emberwind.faq import FAQ, Question, Topic
from emberwind.models.emberwind.news import Article, News
from emberwind.models.emberwind.enums import Order, Sorting, Category


class FAQController:
    """A controller for the FAQ endpoints."""

    @staticmethod
    async def get_all_faqs(
        session: Session,
        url: str,
        keyword: str = "",
        page: int = 0,
        size: int = 10,
    ) -> FAQ:
        """
        Get all FAQs based on the given parameters.
        :param session:
        :param url:
        :param keyword:
        :param page:
        :param size:
        :return:
        """
        response = await session.get(
            f"{url}/content/faq",
            params={
                "keyword": keyword,
                "page": page,
                "size": size,
            },
        )

        return FAQ.from_json(response.json())

    @staticmethod
    async def get_question(session: Session, url: str, slug: str) -> Question:
        """
        Get a question based on the given slug.
        :param session:
        :param url:
        :param slug:
        :return:
        """
        response = await session.get(
            f"{url}/content/faq/{slug}",
        )

        return Question.from_json(response.json())

    @staticmethod
    async def get_top_faqs(
        session: Session,
        url: str,
    ) -> list[Question]:
        """
        Get the top 10 FAQs.
        :param session:
        :param url:
        :return:
        """
        response = await session.get(
            f"{url}/content/faq/top",
        )

        return [Question.from_json(question) for question in response.json()]

    @staticmethod
    async def get_all_topics(
        session: Session,
        url: str,
    ) -> list[Topic]:
        """
        Get all topics.
        :param session:
        :param url:
        :return:
        """
        response = await session.get(
            f"{url}/content/faq/topic",
        )

        return [Topic.from_json(topic) for topic in response.json()]

    @staticmethod
    async def get_topic_navigation(
        session: Session,
        url: str,
    ) -> list[Topic]:
        """
        Get the topic navigation.
        :param session:
        :param url:
        :return:
        """
        response = await session.get(
            f"{url}/content/faq/topic/navigation",
        )

        return [Topic.from_json(topic) for topic in response.json()]

    @staticmethod
    async def get_topic(
        session: Session,
        url: str,
        slug: str,
    ) -> Topic:
        """
        Get a topic based on the given slug.
        :param session:
        :param url:
        :param slug:
        :return:
        """
        response = await session.get(
            f"{url}/content/faq/topic/{slug}",
        )

        return Topic.from_json(response.json())


class NewsController:
    """A controller for the news endpoints."""

    @staticmethod
    async def get_all_news(
        session: Session,
        url: str,
        page: int = 0,
        size: int = 20,
        order_by: Order = Order.TITLE,
        sorting: Sorting = Sorting.DESCENDING,
        categories: list[Category] = None,
        title: str = "",
    ) -> News:
        """
        Get all news based on the given parameters.
        :param session:
        :param url:
        :param page:
        :param size:
        :param order_by:
        :param sorting:
        :param categories:
        :param title:
        :return:
        """
        if categories is None:
            categories = []

        response = await session.get(
            f"{url}/content/news",
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
    async def _get_article_from_slug(session: Session, url: str, slug: str) -> Article:
        """
        Get an article based on the given slug.
        :param session: The session to use.
        :param url: The base URL.
        :param slug: The slug of the article.
        :return: The article.
        """
        response = await session.get(
            f"{url}/content/news/{slug}",
        )

        return Article.from_json(response.json())

    @staticmethod
    async def get_article(
        session: Session, url: str, slug: str = None, article: Article = None
    ) -> Article:
        """
        Get an article based on the given slug or article.
        :param session: The session to use.
        :param url: The base URL.
        :param slug: The slug of the article.
        :param article: The article.
        :return: The article.
        """
        if slug:
            return await NewsController._get_article_from_slug(session, url, slug)

        if article:
            return await NewsController._get_article_from_slug(
                session, url, article.slug
            )
