# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .recipients.slack_channel_data_param import SlackChannelDataParam
from .recipients.discord_channel_data_param import DiscordChannelDataParam
from .recipients.ms_teams_channel_data_param import MsTeamsChannelDataParam

__all__ = [
    "UserSetChannelDataParams",
    "Data",
    "DataPushChannelDataTokensOnly",
    "DataPushChannelDataDevicesOnly",
    "DataPushChannelDataDevicesOnlyDevice",
    "DataAwssnsPushChannelDataTargetArNsOnly",
    "DataAwssnsPushChannelDataDevicesOnly",
    "DataAwssnsPushChannelDataDevicesOnlyDevice",
    "DataOneSignalChannelDataPlayerIDsOnly",
]


class UserSetChannelDataParams(TypedDict, total=False):
    data: Required[Data]
    """Channel data for a given channel type."""


class DataPushChannelDataTokensOnly(TypedDict, total=False):
    tokens: Required[SequenceNotStr[str]]
    """A list of push channel tokens."""


class DataPushChannelDataDevicesOnlyDevice(TypedDict, total=False):
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


class DataPushChannelDataDevicesOnly(TypedDict, total=False):
    devices: Required[Iterable[DataPushChannelDataDevicesOnlyDevice]]
    """A list of devices.

    Each device contains a token, and optionally a locale and timezone.
    """


class DataAwssnsPushChannelDataTargetArNsOnly(TypedDict, total=False):
    target_arns: Required[SequenceNotStr[str]]
    """A list of platform endpoint ARNs.

    See
    [Setting up an Amazon SNS platform endpoint for mobile notifications](https://docs.aws.amazon.com/sns/latest/dg/mobile-platform-endpoint.html).
    """


class DataAwssnsPushChannelDataDevicesOnlyDevice(TypedDict, total=False):
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


class DataAwssnsPushChannelDataDevicesOnly(TypedDict, total=False):
    devices: Required[Iterable[DataAwssnsPushChannelDataDevicesOnlyDevice]]
    """A list of devices.

    Each device contains a target_arn, and optionally a locale and timezone.
    """


class DataOneSignalChannelDataPlayerIDsOnly(TypedDict, total=False):
    player_ids: Required[SequenceNotStr[str]]
    """A list of OneSignal player IDs."""


Data: TypeAlias = Union[
    DataPushChannelDataTokensOnly,
    DataPushChannelDataDevicesOnly,
    DataAwssnsPushChannelDataTargetArNsOnly,
    DataAwssnsPushChannelDataDevicesOnly,
    DataOneSignalChannelDataPlayerIDsOnly,
    SlackChannelDataParam,
    MsTeamsChannelDataParam,
    DiscordChannelDataParam,
]
