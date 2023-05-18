import pytest
from emberwind import Article, News, Category


def test_create_article():
    with pytest.raises(TypeError):
        Article()








def test_create_article_from_json():
    json = {
        "id": 0,
        "slug": "string",
        "title": "string",
        "shortTitle": "string",
        "subTitle": "string",
        "updated": "2023-05-15T23:09:40.830Z",
        "created": "2023-05-15T23:09:40.830Z",
        "thumbnail": {"name": "string", "imageUrl": "string"},
        "categories": [{"id": 1, "name": "string"}],
        "content": "string",
        "heroImage": {"name": "string", "imageUrl": "string"},
        "imagesBaseUrl": "string",
    }

    article = Article.from_json(json)

    assert article.id == 0
    assert article.slug == "string"
    assert article.title == "string"
    assert article.short_title == "string"
    assert article.sub_title == "string"
    assert article.updated == "2023-05-15T23:09:40.830Z"
    assert article.created == "2023-05-15T23:09:40.830Z"
    assert article.thumbnail_name == "string"
    assert article.thumbnail_url == "string"
    assert article.categories[0] == Category.STORE
    assert article.content == "string"
    assert article.hero_image_name == "string"
    assert article.hero_image_url == "string"
    assert article.images_base_url == "string"


def test_create_news():
    with pytest.raises(TypeError):
        News()


def test_create_news_from_json():
    json = {
        "metadata": {"totalElements": 0, "totalPages": 0},
        "data": [
            {
                "id": 0,
                "slug": "string",
                "title": "string",
                "shortTitle": "string",
                "subTitle": "string",
                "updated": "2023-05-15T23:09:40.830Z",
                "created": "2023-05-15T23:09:40.830Z",
                "thumbnail": {"name": "string", "imageUrl": "string"},
                "categories": [{"id": 1, "name": "string"}],
                "content": "string",
                "heroImage": {"name": "string", "imageUrl": "string"},
                "imagesBaseUrl": "string",
            }
        ],
    }

    news = News.from_json(json)

    assert news.total_articles == 0
    assert news.total_pages == 0
    assert len(news.articles) == 1
    assert news.articles[0].id == 0
    assert news.articles[0].slug == "string"
    assert news.articles[0].title == "string"
    assert news.articles[0].short_title == "string"
    assert news.articles[0].sub_title == "string"
    assert news.articles[0].updated == "2023-05-15T23:09:40.830Z"
    assert news.articles[0].created == "2023-05-15T23:09:40.830Z"
    assert news.articles[0].thumbnail_name == "string"
    assert news.articles[0].thumbnail_url == "string"
    assert news.articles[0].categories[0] == Category.STORE
    assert news.articles[0].content == "string"
    assert news.articles[0].hero_image_name == "string"
    assert news.articles[0].hero_image_url == "string"
    assert news.articles[0].images_base_url == "string"
