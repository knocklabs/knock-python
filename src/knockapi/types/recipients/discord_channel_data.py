# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["DiscordChannelData", "Connection", "ConnectionChannelConnection", "ConnectionIncomingWebhookConnection"]


class ConnectionChannelConnection(BaseModel):
    channel_id: str
    """The Discord channel ID"""


class ConnectionIncomingWebhookConnection(BaseModel):
    url: str


Connection: TypeAlias = Union[ConnectionChannelConnection, ConnectionIncomingWebhookConnection]


class DiscordChannelData(BaseModel):
    connections: List[Connection]
