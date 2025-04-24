# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

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
    channel_id: str
    """The unique identifier for the channel."""

    data: Data
    """Channel data for a given channel type."""

    provider: Literal[
        "push_fcm",
        "push_apns",
        "push_expo",
        "push_one_signal",
        "chat_slack",
        "chat_ms_teams",
        "chat_discord",
        "http_knock_webhook",
    ]
    """The type of provider."""

    api_typename: Optional[str] = FieldInfo(alias="__typename", default=None)
    """The typename of the schema."""
