# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AwsSnsPushChannelDataDevicesOnlyParam", "Device"]


class Device(TypedDict, total=False):
    target_arn: Required[str]
    """
    The ARN of a platform endpoint associated with a platform application and a
    device token. See
    [Setting up an Amazon SNS platform endpoint for mobile notifications](https://docs.aws.amazon.com/sns/latest/dg/mobile-platform-endpoint.html).
    """

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


class AwsSnsPushChannelDataDevicesOnlyParam(TypedDict, total=False):
    devices: Required[Iterable[Device]]
    """A list of devices.

    Each device contains a target_arn, and optionally a locale and timezone.
    """
