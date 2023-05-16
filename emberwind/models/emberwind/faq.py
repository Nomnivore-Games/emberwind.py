from __future__ import annotations

from attrs import define


@define
class FAQ:
    """FAQ model."""

    total_questions: int
    """Total number of questions."""
    total_pages: int
    """Total number of pages."""
    questions: list[Question]
    """List of questions."""

    @classmethod
    def from_json(cls, json: dict) -> FAQ:
        """
        Create a FAQ object from a JSON object.
        :param json:
        :return:
        """
        return FAQ(
            total_questions=json["metadata"]["totalElements"],
            total_pages=json["metadata"]["totalPages"],
            questions=[Question.from_json(d) for d in json["data"]],
        )


@define
class Question:
    """Question model."""

    id: int
    """Question ID."""
    slug: str
    """Question slug."""
    question: str
    """Question text."""
    answer: str = ""
    """Answer text."""
    path: list[Path] = []
    """Path to the question."""
    topic: Topic = None
    """Topic of the question."""

    @classmethod
    def from_json(cls, json: dict) -> Question:
        """
        Create a Question object from a JSON object.
        :param json:
        :return:
        """
        return Question(
            id=json["id"],
            slug=json["slug"],
            question=json["question"],
            answer=json.get("answer", ""),
            path=[Path.from_json(d) for d in json["path"]] if "path" in json else [],
            topic=Topic.from_json(json["topic"]) if "topic" in json else None,
        )


@define
class Path:
    """Path model."""

    id: int
    """Path ID."""
    slug: str
    """Path slug."""
    name: str
    """Path name."""

    @classmethod
    def from_json(cls, json: dict) -> Path:
        """
        Create a Path object from a JSON object.
        :param json:
        :return:
        """
        return Path(
            id=json["id"],
            slug=json["slug"],
            name=json["name"],
        )


@define
class Topic:
    """Topic model."""

    id: int
    """Topic ID."""
    slug: str
    """Topic slug."""
    name: str
    """Topic name."""
    icon: str = ""
    """Topic icon."""
    subtopics: list[Topic] = []
    """List of subtopics."""
    entries: list[Question] = []
    """List of questions."""

    @classmethod
    def from_json(cls, json: dict) -> Topic:
        """
        Create a Topic object from a JSON object.
        :param json:
        :return:
        """
        return Topic(
            id=json["id"],
            slug=json["slug"],
            name=json["name"],
            icon=json.get("icon", ""),
            subtopics=[Topic.from_json(d) for d in json["subtopics"]]
            if "subtopics" in json
            else [],
            entries=[Question.from_json(d) for d in json["entries"]]
            if "entries" in json
            else [],
        )
