# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .slack_channel_data_param import SlackChannelDataParam
from .discord_channel_data_param import DiscordChannelDataParam
from .ms_teams_channel_data_param import MsTeamsChannelDataParam

__all__ = [
    "InlineChannelDataRequestParam",
    "InlineChannelDataRequestParamItem",
    "InlineChannelDataRequestParamItemPushChannelDataTokensOnly",
    "InlineChannelDataRequestParamItemAwssnsPushChannelDataTargetArNsOnly",
    "InlineChannelDataRequestParamItemOneSignalChannelDataPlayerIDsOnly",
]


class InlineChannelDataRequestParamItemPushChannelDataTokensOnly(TypedDict, total=False):
    tokens: Required[SequenceNotStr[str]]
    """A list of push channel tokens."""


class InlineChannelDataRequestParamItemAwssnsPushChannelDataTargetArNsOnly(TypedDict, total=False):
    target_arns: Required[SequenceNotStr[str]]
    """A list of platform endpoint ARNs.

    See
    [Setting up an Amazon SNS platform endpoint for mobile notifications](https://docs.aws.amazon.com/sns/latest/dg/mobile-platform-endpoint.html).
    """


class InlineChannelDataRequestParamItemOneSignalChannelDataPlayerIDsOnly(TypedDict, total=False):
    player_ids: Required[SequenceNotStr[str]]
    """A list of OneSignal player IDs."""


InlineChannelDataRequestParamItem: TypeAlias = Union[
    InlineChannelDataRequestParamItemPushChannelDataTokensOnly,
    InlineChannelDataRequestParamItemAwssnsPushChannelDataTargetArNsOnly,
    InlineChannelDataRequestParamItemOneSignalChannelDataPlayerIDsOnly,
    SlackChannelDataParam,
    MsTeamsChannelDataParam,
    DiscordChannelDataParam,
]

InlineChannelDataRequestParam: TypeAlias = Dict[str, InlineChannelDataRequestParamItem]
