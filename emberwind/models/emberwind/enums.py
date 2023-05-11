from enum import Enum, StrEnum


__all__ = [
    "Order",
    "Sorting",
    "Category",
]


class Order(StrEnum):
    """Order enum for sorting articles."""

    TITLE = "title"
    """Sort by title."""
    UPDATED = "updated"
    """Sort by last updated."""


class Sorting(StrEnum):
    """Sorting enum for sorting articles."""

    ASCENDING = "asc"
    """Sort in ascending order."""
    DESCENDING = "desc"
    """Sort in descending order."""


class Category(Enum):
    """Category enum for filtering articles."""

    STORE = 1
    """Store articles."""
    CONVENTIONS = 2
    """Convention articles."""
    CLASSES = 3
    """Class articles."""
    ARCHIVE = 4
    """Archive articles."""
    DLCROUNDUPS = 5
    """DLC round-up articles."""
