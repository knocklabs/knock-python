# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .recipients.inline_channel_data_request_param import InlineChannelDataRequestParam
from .recipients.inline_preference_set_request_param import InlinePreferenceSetRequestParam

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    avatar: Optional[str]
    """URL to the user's avatar image."""

    channel_data: Optional[InlineChannelDataRequestParam]
    """A request to set channel data for a type of channel inline."""

    created_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The creation date of the user from your system."""

    email: Optional[str]
    """The primary email address for the user."""

    locale: Optional[str]
    """The locale of the user.

    Used for [message localization](/concepts/translations).
    """

    name: Optional[str]
    """Display name of the user."""

    phone_number: Optional[str]
    """
    The [E.164](https://www.twilio.com/docs/glossary/what-e164) phone number of the
    user (required for SMS channels).
    """

    preferences: Optional[InlinePreferenceSetRequestParam]
    """Inline set preferences for a recipient, where the key is the preference set id."""

    timezone: Optional[str]
    """The timezone of the user.

    Must be a
    valid [tz database time zone string](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    Used
    for [recurring schedules](/concepts/schedules#scheduling-workflows-with-recurring-schedules-for-recipients).
    """
