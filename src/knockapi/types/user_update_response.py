# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .recipients.channel_data import ChannelData
from .recipients.preference_set import PreferenceSet

__all__ = ["UserUpdateResponse"]


class UserUpdateResponse(BaseModel):
    id: str
    """The ID for the user that you set when identifying them in Knock."""

    created_at: datetime
    """The creation date of the user from your system."""

    updated_at: datetime
    """The timestamp when the resource was last updated."""

    api_typename: Optional[str] = FieldInfo(alias="__typename", default=None)
    """The typename of the schema."""

    avatar: Optional[str] = None
    """URL to the user's avatar image."""

    channel_data: Optional[List[ChannelData]] = None
    """
    Channel-specific information that's needed to deliver a notification to an end
    provider.
    """

    email: Optional[str] = None
    """The primary email address for the user."""

    locale: Optional[str] = None
    """The locale of the user. Used for [message localization](/concepts/translations)"""

    name: Optional[str] = None
    """Display name of the user."""

    phone_number: Optional[str] = None
    """
    The [E.164](https://www.twilio.com/docs/glossary/what-e164) phone number of the
    user (required for SMS channels).
    """

    preferences: Optional[PreferenceSet] = None
    """
    A preference set represents a specific set of notification preferences for a
    recipient. A recipient can have multiple preference sets.
    """

    timezone: Optional[str] = None
    """The timezone of the user.

    Must be a valid
    [tz database time zone string](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    Used for
    [recurring schedules](/concepts/schedules#scheduling-workflows-with-recurring-schedules-for-recipients)
    """
