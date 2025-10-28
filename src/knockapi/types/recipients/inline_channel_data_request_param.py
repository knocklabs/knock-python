# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .slack_channel_data_param import SlackChannelDataParam
from .discord_channel_data_param import DiscordChannelDataParam
from .ms_teams_channel_data_param import MsTeamsChannelDataParam

__all__ = [
    "InlineChannelDataRequestParam",
    "InlineChannelDataRequestParamItem",
    "InlineChannelDataRequestParamItemPushChannelDataTokensOnly",
    "InlineChannelDataRequestParamItemPushChannelDataDevicesOnly",
    "InlineChannelDataRequestParamItemPushChannelDataDevicesOnlyDevice",
    "InlineChannelDataRequestParamItemAwssnsPushChannelDataTargetArNsOnly",
    "InlineChannelDataRequestParamItemAwssnsPushChannelDataDevicesOnly",
    "InlineChannelDataRequestParamItemAwssnsPushChannelDataDevicesOnlyDevice",
    "InlineChannelDataRequestParamItemOneSignalChannelDataPlayerIDsOnly",
]


class InlineChannelDataRequestParamItemPushChannelDataTokensOnly(TypedDict, total=False):
    tokens: Required[SequenceNotStr[str]]
    """A list of push channel tokens."""


class InlineChannelDataRequestParamItemPushChannelDataDevicesOnlyDevice(TypedDict, total=False):
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


class InlineChannelDataRequestParamItemPushChannelDataDevicesOnly(TypedDict, total=False):
    devices: Required[Iterable[InlineChannelDataRequestParamItemPushChannelDataDevicesOnlyDevice]]
    """A list of devices.

    Each device contains a token, and optionally a locale and timezone.
    """


class InlineChannelDataRequestParamItemAwssnsPushChannelDataTargetArNsOnly(TypedDict, total=False):
    target_arns: Required[SequenceNotStr[str]]
    """A list of platform endpoint ARNs.

    See
    [Setting up an Amazon SNS platform endpoint for mobile notifications](https://docs.aws.amazon.com/sns/latest/dg/mobile-platform-endpoint.html).
    """


class InlineChannelDataRequestParamItemAwssnsPushChannelDataDevicesOnlyDevice(TypedDict, total=False):
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


class InlineChannelDataRequestParamItemAwssnsPushChannelDataDevicesOnly(TypedDict, total=False):
    devices: Required[Iterable[InlineChannelDataRequestParamItemAwssnsPushChannelDataDevicesOnlyDevice]]
    """A list of devices.

    Each device contains a target_arn, and optionally a locale and timezone.
    """


class InlineChannelDataRequestParamItemOneSignalChannelDataPlayerIDsOnly(TypedDict, total=False):
    player_ids: Required[SequenceNotStr[str]]
    """A list of OneSignal player IDs."""


InlineChannelDataRequestParamItem: TypeAlias = Union[
    InlineChannelDataRequestParamItemPushChannelDataTokensOnly,
    InlineChannelDataRequestParamItemPushChannelDataDevicesOnly,
    InlineChannelDataRequestParamItemAwssnsPushChannelDataTargetArNsOnly,
    InlineChannelDataRequestParamItemAwssnsPushChannelDataDevicesOnly,
    InlineChannelDataRequestParamItemOneSignalChannelDataPlayerIDsOnly,
    SlackChannelDataParam,
    MsTeamsChannelDataParam,
    DiscordChannelDataParam,
]

InlineChannelDataRequestParam: TypeAlias = Dict[str, InlineChannelDataRequestParamItem]
