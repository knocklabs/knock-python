# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .push_channel_data import PushChannelData
from .slack_channel_data import SlackChannelData
from .discord_channel_data import DiscordChannelData
from .ms_teams_channel_data import MsTeamsChannelData
from .one_signal_channel_data import OneSignalChannelData

__all__ = ["ChannelData", "ChannelDataItem", "ChannelDataItemData"]

ChannelDataItemData: TypeAlias = Union[
    PushChannelData, OneSignalChannelData, SlackChannelData, MsTeamsChannelData, DiscordChannelData
]


class ChannelDataItem(BaseModel):
    channel_id: str
    """The ID of the channel to associate data with."""

    data: ChannelDataItemData
    """Channel data for a given channel type."""

    provider: str
    """The provider identifier (must match the data.type value)"""


ChannelData: TypeAlias = List[ChannelDataItem]
