# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["PushChannelDataDevicesOnlyParam", "Device"]


class Device(TypedDict, total=False):
    token: Required[str]
    """The device token to send the push notification to."""

    locale: Optional[str]
    """The locale of the object.

    Used for [message localization](/concepts/translations).
    """

    timezone: Optional[str]
    """The timezone of the object.

    Must be a
    valid [tz database time zone string](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    Used
    for [recurring schedules](/concepts/schedules#scheduling-workflows-with-recurring-schedules-for-recipients).
    """


class PushChannelDataDevicesOnlyParam(TypedDict, total=False):
    """Push channel data."""

    devices: Required[Iterable[Device]]
    """A list of devices.

    Each device contains a token, and optionally a locale and timezone.
    """
