# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Object"]


class Object(BaseModel):
    id: str
    """Unique identifier for the object."""

    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    collection: str
    """The collection this object belongs to."""

    updated_at: datetime
    """The timestamp when the resource was last updated."""

    created_at: Optional[datetime] = None
    """Timestamp when the resource was created."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
