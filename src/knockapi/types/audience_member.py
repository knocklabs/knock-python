# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .user import User
from .._models import BaseModel

__all__ = ["AudienceMember"]


class AudienceMember(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")
    """The type name of the schema."""

    added_at: datetime
    """Timestamp when the resource was created."""

    user: User
    """A user object."""

    user_id: str
    """The unique identifier for the user."""

    tenant: Optional[str] = None
    """The unique identifier for the tenant."""
