# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "SlackChannelDataParam",
    "Connection",
    "ConnectionSlackTokenConnection",
    "ConnectionSlackIncomingWebhookConnection",
    "Token",
]


class ConnectionSlackTokenConnection(TypedDict, total=False):
    access_token: Optional[str]
    """A Slack access token."""

    channel_id: Optional[str]
    """A Slack channel ID from the Slack provider."""

    user_id: Optional[str]
    """A Slack user ID from the Slack provider."""


class ConnectionSlackIncomingWebhookConnection(TypedDict, total=False):
    url: Required[str]
    """The URL of the incoming webhook for a Slack connection."""


Connection: TypeAlias = Union[ConnectionSlackTokenConnection, ConnectionSlackIncomingWebhookConnection]


class Token(TypedDict, total=False):
    access_token: Required[Optional[str]]
    """A Slack access token."""


class SlackChannelDataParam(TypedDict, total=False):
    connections: Required[Iterable[Connection]]
    """List of Slack channel connections."""

    token: Optional[Token]
    """A Slack connection token."""
