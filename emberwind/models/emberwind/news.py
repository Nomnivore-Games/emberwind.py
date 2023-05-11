import attrs
from emberwind.models.emberwind import article
from emberwind.models.emberwind.article import Article

__all__ = [
    "News",
    "from_json",
]


@attrs.define
class News:
    """News model."""

    total_articles: int
    """Total number of articles."""
    total_pages: int
    """Total number of pages."""
    articles: list[Article]
    """List of articles."""


def from_json(json: dict) -> News:
    """
    Create a News object from a JSON object.
    :param json:
    :return News:
    """
    return News(
        total_articles=json["metadata"]["totalElements"],
        total_pages=json["metadata"]["totalPages"],
        articles=[article.from_json(a) for a in json["data"]],
    )
