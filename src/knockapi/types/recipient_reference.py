# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["RecipientReference", "ObjectReference"]


class ObjectReference(BaseModel):
    id: Optional[str] = None
    """An identifier for the recipient object."""

    collection: Optional[str] = None
    """The collection the recipient object belongs to."""


RecipientReference: TypeAlias = Union[str, ObjectReference]
