# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "SlackChannelData",
    "Connection",
    "ConnectionSlackTokenConnection",
    "ConnectionSlackIncomingWebhookConnection",
    "Token",
]


class ConnectionSlackTokenConnection(TypedDict, total=False):
    access_token: Optional[str]

    channel_id: Optional[str]

    user_id: Optional[str]


class ConnectionSlackIncomingWebhookConnection(TypedDict, total=False):
    url: Required[str]


Connection: TypeAlias = Union[ConnectionSlackTokenConnection, ConnectionSlackIncomingWebhookConnection]


class Token(TypedDict, total=False):
    access_token: Required[Optional[str]]


class SlackChannelData(TypedDict, total=False):
    connections: Required[Iterable[Connection]]

    token: Optional[Token]
    """A token that's used to store the access token for a Slack workspace."""
