from attrs import asdict, define, make_class, Factory
from emberwind.models.emberwind.enums import Category

__all__ = [
    "Article",
]


@define
class Article:
    """Article model."""

    id: int
    """Article ID."""
    slug: str
    """Article slug."""
    title: str
    """Article title."""
    short_title: str
    """Article short title."""
    sub_title: str
    """Article sub title."""
    updated: str
    """Article last updated."""
    created: str
    """Article creation date."""
    thumbnail_name: str
    """Article thumbnail name."""
    thumbnail_url: str
    """Article thumbnail URL."""
    categories: list[Category]
    """Article categories."""
    content: str
    """Article content."""
    hero_image_name: str
    """Article hero image name."""
    hero_image_url: str
    """Article hero image URL."""
    images_base_url: str
    """Article images base URL."""

    @classmethod
    def from_json(cls, json: dict) -> Article:
        """
        Create an Article from a JSON object.
        :param json:
        :return Article:
        """
        return cls(
            id=json["id"],
            slug=json["slug"],
            title=json["title"],
            short_title=json["shortTitle"],
            sub_title=json["subTitle"],
            updated=json["updated"],
            created=json["created"],
            thumbnail_name=json["thumbnail"]["name"],
            thumbnail_url=json["thumbnail"]["imageUrl"],
            categories=[Category(c["id"]) for c in json["categories"]],
            content=json.get("content", None),
            hero_image_name=json.get("heroImage", {}).get("name", None),
            hero_image_url=json.get("heroImage", {}).get("imageUrl", None),
            images_base_url=json.get("imagesBaseUrl", None),
        )
