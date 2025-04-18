# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "SlackChannelData",
    "Token",
    "Connection",
    "ConnectionSlackTokenConnection",
    "ConnectionSlackIncomingWebhookConnection",
]


class Token(BaseModel):
    access_token: Optional[str] = None
    """A Slack access token."""


class ConnectionSlackTokenConnection(BaseModel):
    access_token: Optional[str] = None
    """A Slack access token."""

    channel_id: Optional[str] = None
    """A Slack channel ID from the Slack provider."""

    user_id: Optional[str] = None
    """A Slack user ID from the Slack provider."""


class ConnectionSlackIncomingWebhookConnection(BaseModel):
    url: str
    """The URL of the incoming webhook for a Slack connection."""


Connection: TypeAlias = Union[ConnectionSlackTokenConnection, ConnectionSlackIncomingWebhookConnection]


class SlackChannelData(BaseModel):
    token: Optional[Token] = None
    """A Slack connection token."""

    connections: Optional[List[Connection]] = None
    """List of Slack channel connections."""
