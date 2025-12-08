# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "DiscordChannelDataParam",
    "Connection",
    "ConnectionDiscordChannelConnection",
    "ConnectionDiscordIncomingWebhookConnection",
    "ConnectionDiscordIncomingWebhookConnectionIncomingWebhook",
]


class ConnectionDiscordChannelConnection(TypedDict, total=False):
    """Discord channel connection."""

    channel_id: Required[str]
    """Discord channel ID."""


class ConnectionDiscordIncomingWebhookConnectionIncomingWebhook(TypedDict, total=False):
    """Discord incoming webhook object."""

    url: Required[str]
    """Incoming webhook URL."""


class ConnectionDiscordIncomingWebhookConnection(TypedDict, total=False):
    """Discord incoming webhook connection."""

    incoming_webhook: Required[ConnectionDiscordIncomingWebhookConnectionIncomingWebhook]
    """Discord incoming webhook object."""


Connection: TypeAlias = Union[ConnectionDiscordChannelConnection, ConnectionDiscordIncomingWebhookConnection]


class DiscordChannelDataParam(TypedDict, total=False):
    """Discord channel data."""

    connections: Required[Iterable[Connection]]
    """List of Discord channel connections."""
