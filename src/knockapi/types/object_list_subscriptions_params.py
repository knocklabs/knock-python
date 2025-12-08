# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr
from .recipient_reference_param import RecipientReferenceParam

__all__ = ["ObjectListSubscriptionsParams", "Object"]


class ObjectListSubscriptionsParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    include: List[Literal["preferences"]]
    """Additional fields to include in the response."""

    mode: Literal["recipient", "object"]
    """Mode of the request.

    `recipient` to list the objects that the provided object is subscribed to,
    `object` to list the recipients that subscribe to the provided object.
    """

    objects: Iterable[Object]
    """Objects to filter by (only used if mode is `recipient`)."""

    page_size: int
    """The number of items per page (defaults to 50)."""

    recipients: SequenceNotStr[RecipientReferenceParam]
    """Recipients to filter by (only used if mode is `object`)."""


class Object(TypedDict, total=False):
    """A reference to a recipient object."""

    id: str
    """An identifier for the recipient object."""

    collection: str
    """The collection the recipient object belongs to."""
