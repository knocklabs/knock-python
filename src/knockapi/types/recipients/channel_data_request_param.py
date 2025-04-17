# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .push_channel_data_param import PushChannelDataParam
from .slack_channel_data_param import SlackChannelDataParam
from .discord_channel_data_param import DiscordChannelDataParam
from .ms_teams_channel_data_param import MsTeamsChannelDataParam
from .one_signal_channel_data_param import OneSignalChannelDataParam

__all__ = ["ChannelDataRequestParam", "Data"]

Data: TypeAlias = Union[
    PushChannelDataParam,
    OneSignalChannelDataParam,
    SlackChannelDataParam,
    MsTeamsChannelDataParam,
    DiscordChannelDataParam,
]


class ChannelDataRequestParam(TypedDict, total=False):
    data: Required[Data]
    """Channel data for a given channel type."""
