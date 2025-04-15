# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "DiscordChannelDataParam",
    "Connection",
    "ConnectionChannelConnection",
    "ConnectionIncomingWebhookConnection",
]


class ConnectionChannelConnection(TypedDict, total=False):
    channel_id: Required[str]
    """The Discord channel ID"""


class ConnectionIncomingWebhookConnection(TypedDict, total=False):
    url: Required[str]


Connection: TypeAlias = Union[ConnectionChannelConnection, ConnectionIncomingWebhookConnection]


class DiscordChannelDataParam(TypedDict, total=False):
    connections: Required[Iterable[Connection]]
