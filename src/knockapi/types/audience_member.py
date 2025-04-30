# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .user import User
from .._models import BaseModel

__all__ = ["AudienceMember"]


class AudienceMember(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    added_at: datetime
    """Timestamp when the resource was created."""

    user: User
    """
    A [User](/concepts/users) represents an individual in your system who can
    receive notifications through Knock. Users are the most common recipients of
    notifications and are always referenced by your internal identifier.
    """

    user_id: str
    """The ID for the user that you set when identifying them in Knock."""

    tenant: Optional[str] = None
    """The unique identifier for the tenant."""
