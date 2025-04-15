# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "SlackChannelDataParam",
    "Connection",
    "ConnectionTokenConnection",
    "ConnectionIncomingWebhookConnection",
    "Token",
]


class ConnectionTokenConnection(TypedDict, total=False):
    access_token: Optional[str]

    channel_id: Optional[str]

    user_id: Optional[str]


class ConnectionIncomingWebhookConnection(TypedDict, total=False):
    url: Required[str]


Connection: TypeAlias = Union[ConnectionTokenConnection, ConnectionIncomingWebhookConnection]


class Token(TypedDict, total=False):
    access_token: Required[Optional[str]]


class SlackChannelDataParam(TypedDict, total=False):
    connections: Required[Iterable[Connection]]

    token: Optional[Token]
