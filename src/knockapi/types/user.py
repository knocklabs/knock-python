# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    id: str
    """The ID for the user that you set when identifying them in Knock."""

    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    updated_at: datetime
    """The timestamp when the resource was last updated."""

    avatar: Optional[str] = None
    """URL to the user's avatar image."""

    created_at: Optional[datetime] = None
    """The creation date of the user from your system."""

    email: Optional[str] = None
    """The primary email address for the user."""

    name: Optional[str] = None
    """Display name of the user."""

    phone_number: Optional[str] = None
    """
    The [E.164](https://www.twilio.com/docs/glossary/what-e164) phone number of the
    user (required for SMS channels).
    """

    timezone: Optional[str] = None
    """The timezone of the user.

    Must be a
    valid [tz database time zone string](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    Used
    for [recurring schedules](/concepts/schedules#scheduling-workflows-with-recurring-schedules-for-recipients).
    """

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
