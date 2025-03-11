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
    channel_id: Required[str]
    """The Discord channel ID"""


class ConnectionDiscordIncomingWebhookConnectionIncomingWebhook(TypedDict, total=False):
    url: Required[str]
    """The URL of the incoming webhook"""


class ConnectionDiscordIncomingWebhookConnection(TypedDict, total=False):
    incoming_webhook: Required[ConnectionDiscordIncomingWebhookConnectionIncomingWebhook]
    """The incoming webhook"""


Connection: TypeAlias = Union[ConnectionDiscordChannelConnection, ConnectionDiscordIncomingWebhookConnection]


class DiscordChannelDataParam(TypedDict, total=False):
    connections: Required[Iterable[Connection]]
