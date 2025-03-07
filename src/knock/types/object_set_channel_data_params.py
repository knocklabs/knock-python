# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params.push_channel_data import PushChannelData
from .shared_params.slack_channel_data import SlackChannelData
from .shared_params.discord_channel_data import DiscordChannelData
from .shared_params.ms_teams_channel_data import MsTeamsChannelData
from .shared_params.one_signal_channel_data import OneSignalChannelData

__all__ = ["ObjectSetChannelDataParams", "Data"]


class ObjectSetChannelDataParams(TypedDict, total=False):
    collection: Required[str]

    object_id: Required[str]

    data: Required[Data]
    """Channel data for push providers"""


Data: TypeAlias = Union[PushChannelData, OneSignalChannelData, SlackChannelData, MsTeamsChannelData, DiscordChannelData]
