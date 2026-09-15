# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "DiscordChannelData",
    "Connection",
    "ConnectionDiscordChannelConnection",
    "ConnectionDiscordIncomingWebhookConnection",
    "ConnectionDiscordIncomingWebhookConnectionIncomingWebhook",
]


class ConnectionDiscordChannelConnection(BaseModel):
    """Discord channel connection."""

    channel_id: str
    """Discord channel ID."""

    knock_tenant_id: Optional[str] = None
    """An optional Knock tenant ID (`knock_tenant_id`) that scopes this connection.

    Distinct from provider-specific tenant IDs. When a workflow is triggered with
    this tenant, Knock prefers this connection over untagged connections.
    """


class ConnectionDiscordIncomingWebhookConnectionIncomingWebhook(BaseModel):
    """Discord incoming webhook object."""

    url: str
    """Incoming webhook URL."""


class ConnectionDiscordIncomingWebhookConnection(BaseModel):
    """Discord incoming webhook connection."""

    incoming_webhook: ConnectionDiscordIncomingWebhookConnectionIncomingWebhook
    """Discord incoming webhook object."""

    knock_tenant_id: Optional[str] = None
    """An optional Knock tenant ID (`knock_tenant_id`) that scopes this connection.

    Distinct from provider-specific tenant IDs. When a workflow is triggered with
    this tenant, Knock prefers this connection over untagged connections.
    """


Connection: TypeAlias = Union[ConnectionDiscordChannelConnection, ConnectionDiscordIncomingWebhookConnection]


class DiscordChannelData(BaseModel):
    """Discord channel data."""

    connections: List[Connection]
    """List of Discord channel connections."""
