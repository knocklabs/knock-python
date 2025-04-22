# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DiscordChannelData",
    "Connection",
    "ConnectionDiscordChannelConnection",
    "ConnectionDiscordIncomingWebhookConnection",
    "ConnectionDiscordIncomingWebhookConnectionIncomingWebhook",
]


class ConnectionDiscordChannelConnection(BaseModel):
    channel_id: str
    """Discord channel ID."""


class ConnectionDiscordIncomingWebhookConnectionIncomingWebhook(BaseModel):
    url: str
    """Incoming webhook URL."""


class ConnectionDiscordIncomingWebhookConnection(BaseModel):
    incoming_webhook: ConnectionDiscordIncomingWebhookConnectionIncomingWebhook
    """Discord incoming webhook object."""


Connection: TypeAlias = Union[ConnectionDiscordChannelConnection, ConnectionDiscordIncomingWebhookConnection]


class DiscordChannelData(BaseModel):
    api_typename: Literal["DiscordChannelData"] = FieldInfo(alias="__typename")
    """The typename of the schema."""

    connections: List[Connection]
    """List of Discord channel connections."""
