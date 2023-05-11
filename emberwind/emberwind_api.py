import aiohttp
from enum import Enum
from dataclasses import dataclass


class Order(Enum):
    TITLE = 'title'
    UPDATED = 'updated'


class Sorting(Enum):
    ASCENDING = 'asc'
    DESCENDING = 'desc'


class Category(Enum):
    STORE = 1
    CONVENTIONS = 2
    CLASSES = 3
    ARCHIVE = 4
    DLCROUNDUPS = 5


@dataclass()
class Article:
    id: int
    slug: str
    title: str
    short_title: str
    sub_title: str
    updated: str
    created: str
    thumbnail_name: str
    thumbnail_url: str
    categories: list[Category]
    content: str
    hero_image_name: str
    hero_image_url: str
    images_base_url: str


@dataclass()
class News:
    total_articles: int
    total_pages: int
    articles: list[Article]


def _json_to_article(json: dict) -> Article:
    article = Article(
        id=json['id'],
        slug=json['slug'],
        title=json['title'],
        short_title=json['shortTitle'],
        sub_title=json['subTitle'],
        updated=json['updated'],
        created=json['created'],
        thumbnail_name=json['thumbnail']['name'],
        thumbnail_url=json['thumbnail']['imageUrl'],
        categories=[Category(c['id']) for c in json['categories']],
        content=json.get('content', None),
        hero_image_name=json.get('heroImage', {}).get('name', None),
        hero_image_url=json.get('heroImage', {}).get('imageUrl', None),
        images_base_url=json.get('imagesBaseUrl', None),
    )

    return article


def _json_to_news(json: dict) -> News:
    news = News(
        total_articles=json['metadata']['totalElements'],
        total_pages=json['metadata']['totalPages'],
        articles=[_json_to_article(a) for a in json['data']]
    )

    return news


class EmberwindClient:

    def __init__(self, api_key: str):
        self._key = api_key

    def get_all_news(self, page: int = 0, size: int = 20, order_by: Order = Order.TITLE,
                     sorting: Sorting = Sorting.DESCENDING, categories: list[Category] = None, title: str = '') -> News:
        if categories is None:
            categories = []

        r = requests.get(
            'http://emberwind.gflcdevelopment.com/emberwind-web/api/v1/web/content/news',
            params={
                'page': page,
                'size': size,
                'orderBy': order_by.value,
                'ordering': sorting.value,
                'categories': [c.value for c in categories],
                'title': title,
            },
            headers={
                'Emberwind-Api-Key': self._key
            }
        )

        return _json_to_news(r.json())

    def _get_article_from_slug(self, slug: str) -> Article:
        r = requests.get(
            'http://emberwind.gflcdevelopment.com/emberwind-web/api/v1/web/content/news/' + slug,
            headers={
                'Emberwind-Api-Key': self._key
            }
        )

        return _json_to_article(r.json())

    def get_article(self, slug: str = None, article: Article = None) -> Article:
        if slug:
            return self._get_article_from_slug(slug)

        if article:
            return self._get_article_from_slug(article.slug)
