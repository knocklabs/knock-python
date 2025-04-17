# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, TypeAlias, TypedDict

__all__ = ["UserListSubscriptionsParams", "Object", "ObjectObjectReference"]


class UserListSubscriptionsParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    include: List[Literal["preferences"]]
    """Includes preferences of the recipient subscribers in the response."""

    objects: List[Object]
    """Objects to filter by."""

    page_size: int
    """The number of items per page."""


class ObjectObjectReference(TypedDict, total=False):
    id: str
    """An identifier for the recipient object."""

    collection: str
    """The collection the recipient object belongs to."""


Object: TypeAlias = Union[str, ObjectObjectReference]
