import pytest
from emberwind import Article, News


def test_create_article():
    with pytest.raises(TypeError):
        article = Article()


def test_create_news():
    with pytest.raises(TypeError):
        news = News()
