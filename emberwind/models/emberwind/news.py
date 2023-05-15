from __future__ import annotations

import attrs
from emberwind.models.emberwind.article import Article

__all__ = [
    "News",
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

    @classmethod
    def from_json(cls, json: dict) -> News:
        """
        Create a News object from a JSON object.
        :param json:
        :return News:
        """
        return News(
            total_articles=json["metadata"]["totalElements"],
            total_pages=json["metadata"]["totalPages"],
            articles=[Article.from_json(d) for d in json["data"]],
        )
