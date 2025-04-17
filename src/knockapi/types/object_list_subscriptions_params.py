# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ObjectListSubscriptionsParams", "Object", "ObjectObjectReference", "Recipient", "RecipientObjectReference"]


class ObjectListSubscriptionsParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    include: List[Literal["preferences"]]
    """Includes preferences of the recipient subscribers in the response."""

    mode: Literal["recipient", "object"]
    """Mode of the request."""

    objects: List[Object]
    """Objects to filter by (only used if mode is `recipient`)."""

    page_size: int
    """The number of items per page."""

    recipients: List[Recipient]
    """Recipients to filter by (only used if mode is `object`)."""


class ObjectObjectReference(TypedDict, total=False):
    id: Required[str]
    """An identifier for the recipient object."""

    collection: Required[str]
    """The collection the recipient object belongs to."""


Object: TypeAlias = Union[str, ObjectObjectReference]


class RecipientObjectReference(TypedDict, total=False):
    id: Required[str]
    """An identifier for the recipient object."""

    collection: Required[str]
    """The collection the recipient object belongs to."""


Recipient: TypeAlias = Union[str, RecipientObjectReference]
