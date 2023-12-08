from __future__ import annotations

from attrs import define


@define
class User:
    """User model."""

    id: int
    """User ID."""
    email: str
    """User email."""
    first_name: str
    """User first name."""
    last_name: str
    """User last name."""
    digital_content_available: bool
    """Digital content availability."""
    hero_creator_available: bool
    """Hero creator availability."""
    accepted_dev_eula: bool
    """Accepted dev EULA."""
    attached_api_key: bool
    """Attached API key."""
    username: str
    """User's username."""
    editable_username: bool
    """If the username is editable."""

    @classmethod
    def from_json(cls, json: dict) -> User:
        """
        Create a user object from a JSON object.
        :param json:
        :return:
        """
        return User(
            id=json["id"],
            email=json["email"],
            first_name=json["firstName"],
            last_name=json["lastName"],
            digital_content_available=json["digitalContentAvailable"],
            hero_creator_available=json["heroCreatorAvailable"],
            accepted_dev_eula=json["acceptedDevEula"],
            attached_api_key=json["attachedApiKey"],
            username=json["username"],
            editable_username=json["editableUsername"],
        )
