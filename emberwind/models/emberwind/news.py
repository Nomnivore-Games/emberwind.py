from attrs import asdict, define, make_class, Factory
from emberwind.models.emberwind.article import Article

__all__ = [
    "News",
]


@define
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
        return cls(
            total_articles=json["metadata"]["totalElements"],
            total_pages=json["metadata"]["totalPages"],
            articles=[Article.from_json(a) for a in json["data"]],
        )
