# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    id: str
    """The unique identifier for the user."""

    api_typename: str = FieldInfo(alias="__typename")
    """The type name of the schema."""

    updated_at: datetime
    """The timestamp when the resource was last updated."""

    avatar: Optional[str] = None
    """URL to the user's avatar image."""

    created_at: Optional[datetime] = None
    """Timestamp when the resource was created."""

    email: Optional[str] = None
    """The email address of the user."""

    name: Optional[str] = None
    """Display name of the user."""

    phone_number: Optional[str] = None
    """Phone number of the user."""

    timezone: Optional[str] = None
    """Timezone of the user."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
