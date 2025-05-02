# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .recipients.inline_channel_data_request_param import InlineChannelDataRequestParam
from .recipients.inline_preference_set_request_param import InlinePreferenceSetRequestParam

__all__ = ["ObjectSetParams"]


class ObjectSetParams(TypedDict, total=False):
    channel_data: InlineChannelDataRequestParam
    """A request to set channel data for a type of channel inline."""

    locale: Optional[str]
    """The locale of the object.

    Used for [message localization](/concepts/translations).
    """

    preferences: InlinePreferenceSetRequestParam
    """Inline set preferences for a recipient, where the key is the preference set id."""

    timezone: Optional[str]
    """The timezone of the object.

    Must be a
    valid [tz database time zone string](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    Used
    for [recurring schedules](/concepts/schedules#scheduling-workflows-with-recurring-schedules-for-recipients).
    """
