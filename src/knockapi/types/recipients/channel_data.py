# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .push_channel_data import PushChannelData
from .slack_channel_data import SlackChannelData
from .discord_channel_data import DiscordChannelData
from .ms_teams_channel_data import MsTeamsChannelData
from .one_signal_channel_data import OneSignalChannelData

__all__ = ["ChannelData", "Data"]

Data: TypeAlias = Union[PushChannelData, SlackChannelData, MsTeamsChannelData, DiscordChannelData, OneSignalChannelData]


class ChannelData(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")
    """The type name of the schema."""

    channel_id: str
    """The unique identifier for the channel."""

    data: Data
    """Channel data for a given channel type."""
