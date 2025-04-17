# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "SlackChannelData",
    "Connection",
    "ConnectionSlackTokenConnection",
    "ConnectionSlackIncomingWebhookConnection",
    "Token",
]


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


class Token(BaseModel):
    access_token: Optional[str] = None
    """A Slack access token."""


class SlackChannelData(BaseModel):
    connections: List[Connection]
    """List of Slack channel connections."""

    token: Optional[Token] = None
    """A Slack connection token."""
