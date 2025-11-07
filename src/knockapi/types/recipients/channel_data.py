# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .slack_channel_data import SlackChannelData
from .discord_channel_data import DiscordChannelData
from .ms_teams_channel_data import MsTeamsChannelData
from .one_signal_channel_data_player_ids_only import OneSignalChannelDataPlayerIDsOnly

__all__ = [
    "ChannelData",
    "Data",
    "DataPushChannelDataFull",
    "DataPushChannelDataFullDevice",
    "DataAwssnsPushChannelDataFull",
    "DataAwssnsPushChannelDataFullDevice",
]


class DataPushChannelDataFullDevice(BaseModel):
    token: str
    """The device token to send the push notification to."""

    locale: Optional[str] = None
    """The locale of the object.

    Used for [message localization](/concepts/translations).
    """

    timezone: Optional[str] = None
    """The timezone of the object.

    Must be a
    valid [tz database time zone string](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    Used
    for [recurring schedules](/concepts/schedules#scheduling-workflows-with-recurring-schedules-for-recipients).
    """


class DataPushChannelDataFull(BaseModel):
    devices: List[DataPushChannelDataFullDevice]
    """A list of devices.

    Each device contains a token, and optionally a locale and timezone.
    """

    tokens: List[str]
    """A list of push channel tokens."""


class DataAwssnsPushChannelDataFullDevice(BaseModel):
    target_arn: str
    """
    The ARN of a platform endpoint associated with a platform application and a
    device token. See
    [Setting up an Amazon SNS platform endpoint for mobile notifications](https://docs.aws.amazon.com/sns/latest/dg/mobile-platform-endpoint.html).
    """

    locale: Optional[str] = None
    """The locale of the object.

    Used for [message localization](/concepts/translations).
    """

    timezone: Optional[str] = None
    """The timezone of the object.

    Must be a
    valid [tz database time zone string](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    Used
    for [recurring schedules](/concepts/schedules#scheduling-workflows-with-recurring-schedules-for-recipients).
    """


class DataAwssnsPushChannelDataFull(BaseModel):
    devices: List[DataAwssnsPushChannelDataFullDevice]
    """A list of devices.

    Each device contains a target_arn, and optionally a locale and timezone.
    """

    target_arns: List[str]
    """A list of platform endpoint ARNs.

    See
    [Setting up an Amazon SNS platform endpoint for mobile notifications](https://docs.aws.amazon.com/sns/latest/dg/mobile-platform-endpoint.html).
    """


Data: TypeAlias = Union[
    DataPushChannelDataFull,
    DataAwssnsPushChannelDataFull,
    OneSignalChannelDataPlayerIDsOnly,
    SlackChannelData,
    MsTeamsChannelData,
    DiscordChannelData,
]


class ChannelData(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    channel_id: str
    """The unique identifier for the channel."""

    data: Data
    """Channel data for a given channel type."""

    provider: Optional[
        Literal[
            "push_fcm",
            "push_apns",
            "push_aws_sns",
            "push_expo",
            "push_one_signal",
            "chat_slack",
            "chat_ms_teams",
            "chat_discord",
            "http_knock_webhook",
        ]
    ] = None
    """The type of provider."""
