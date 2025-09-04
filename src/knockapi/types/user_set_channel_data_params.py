# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .recipients.push_channel_data_param import PushChannelDataParam
from .recipients.slack_channel_data_param import SlackChannelDataParam
from .recipients.discord_channel_data_param import DiscordChannelDataParam
from .recipients.ms_teams_channel_data_param import MsTeamsChannelDataParam
from .recipients.one_signal_channel_data_param import OneSignalChannelDataParam

__all__ = ["UserSetChannelDataParams", "Data"]


class UserSetChannelDataParams(TypedDict, total=False):
    data: Required[Data]
    """Channel data for a given channel type."""


Data: TypeAlias = Union[
    PushChannelDataParam,
    OneSignalChannelDataParam,
    SlackChannelDataParam,
    MsTeamsChannelDataParam,
    DiscordChannelDataParam,
]
