# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .push_channel_data_param import PushChannelDataParam
from .slack_channel_data_param import SlackChannelDataParam
from .discord_channel_data_param import DiscordChannelDataParam
from .ms_teams_channel_data_param import MsTeamsChannelDataParam
from .one_signal_channel_data_param import OneSignalChannelDataParam

__all__ = [
    "InlineChannelDataRequestParam",
    "InlineChannelDataRequestParamItem",
    "InlineChannelDataRequestParamItemAwsSnsPushChannelData",
]


class InlineChannelDataRequestParamItemAwsSnsPushChannelData(TypedDict, total=False):
    target_arns: Required[SequenceNotStr[str]]
    """A list of platform endpoint ARNs.

    See
    [Setting up an Amazon SNS platform endpoint for mobile notifications](https://docs.aws.amazon.com/sns/latest/dg/mobile-platform-endpoint.html).
    """


InlineChannelDataRequestParamItem: TypeAlias = Union[
    PushChannelDataParam,
    OneSignalChannelDataParam,
    InlineChannelDataRequestParamItemAwsSnsPushChannelData,
    SlackChannelDataParam,
    MsTeamsChannelDataParam,
    DiscordChannelDataParam,
]

InlineChannelDataRequestParam: TypeAlias = Dict[str, InlineChannelDataRequestParamItem]
