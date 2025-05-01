# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias, TypedDict

__all__ = ["RecipientReferenceParam", "ObjectReference"]


class ObjectReference(TypedDict, total=False):
    id: str
    """An identifier for the recipient object."""

    collection: str
    """The collection the recipient object belongs to."""


RecipientReferenceParam: TypeAlias = Union[str, ObjectReference]
