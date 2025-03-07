# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .push_channel_data import PushChannelData
from .slack_channel_data import SlackChannelData
from .discord_channel_data import DiscordChannelData
from .ms_teams_channel_data import MsTeamsChannelData
from .one_signal_channel_data import OneSignalChannelData

__all__ = ["ChannelDataRequest", "Data"]

Data: TypeAlias = Union[PushChannelData, OneSignalChannelData, SlackChannelData, MsTeamsChannelData, DiscordChannelData]


class ChannelDataRequest(TypedDict, total=False):
    data: Required[Data]
    """Channel data for push providers"""
