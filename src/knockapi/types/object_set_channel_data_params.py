# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .recipients.slack_channel_data_param import SlackChannelDataParam
from .recipients.discord_channel_data_param import DiscordChannelDataParam
from .recipients.ms_teams_channel_data_param import MsTeamsChannelDataParam

__all__ = [
    "ObjectSetChannelDataParams",
    "Data",
    "DataPushChannelDataTokensOnly",
    "DataAwssnsPushChannelDataTargetArNsOnly",
    "DataOneSignalChannelDataPlayerIDsOnly",
]


class ObjectSetChannelDataParams(TypedDict, total=False):
    data: Required[Data]
    """Channel data for a given channel type."""


class DataPushChannelDataTokensOnly(TypedDict, total=False):
    tokens: Required[SequenceNotStr[str]]
    """A list of push channel tokens."""


class DataAwssnsPushChannelDataTargetArNsOnly(TypedDict, total=False):
    target_arns: Required[SequenceNotStr[str]]
    """A list of platform endpoint ARNs.

    See
    [Setting up an Amazon SNS platform endpoint for mobile notifications](https://docs.aws.amazon.com/sns/latest/dg/mobile-platform-endpoint.html).
    """


class DataOneSignalChannelDataPlayerIDsOnly(TypedDict, total=False):
    player_ids: Required[SequenceNotStr[str]]
    """A list of OneSignal player IDs."""


Data: TypeAlias = Union[
    DataPushChannelDataTokensOnly,
    DataAwssnsPushChannelDataTargetArNsOnly,
    DataOneSignalChannelDataPlayerIDsOnly,
    SlackChannelDataParam,
    MsTeamsChannelDataParam,
    DiscordChannelDataParam,
]
