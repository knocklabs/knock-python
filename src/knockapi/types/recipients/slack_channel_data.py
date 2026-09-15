# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "SlackChannelData",
    "Connection",
    "ConnectionSlackTokenConnection",
    "ConnectionSlackIncomingWebhookConnection",
    "ConnectionSlackIncomingWebhookConnectionIncomingWebhook",
    "Token",
]


class ConnectionSlackTokenConnection(BaseModel):
    """A Slack connection token."""

    access_token: Optional[str] = None
    """A Slack access token."""

    channel_id: Optional[str] = None
    """A Slack channel ID from the Slack provider."""

    channel_name: Optional[str] = None
    """Slack channel name."""

    knock_tenant_id: Optional[str] = None
    """An optional Knock tenant ID (`knock_tenant_id`) that scopes this connection.

    Distinct from provider-specific tenant IDs. When a workflow is triggered with
    this tenant, Knock prefers this connection over untagged connections.
    """

    user_id: Optional[str] = None
    """A Slack user ID from the Slack provider."""


class ConnectionSlackIncomingWebhookConnectionIncomingWebhook(BaseModel):
    """A Slack connection incoming webhook."""

    url: str
    """The URL of the incoming webhook for a Slack connection."""


class ConnectionSlackIncomingWebhookConnection(BaseModel):
    """A Slack connection incoming webhook."""

    incoming_webhook: ConnectionSlackIncomingWebhookConnectionIncomingWebhook
    """A Slack connection incoming webhook."""

    knock_tenant_id: Optional[str] = None
    """An optional Knock tenant ID (`knock_tenant_id`) that scopes this connection.

    Distinct from provider-specific tenant IDs. When a workflow is triggered with
    this tenant, Knock prefers this connection over untagged connections.
    """


Connection: TypeAlias = Union[ConnectionSlackTokenConnection, ConnectionSlackIncomingWebhookConnection]


class Token(BaseModel):
    """A Slack connection token."""

    access_token: Optional[str] = None
    """A Slack access token."""


class SlackChannelData(BaseModel):
    """Slack channel data."""

    connections: List[Connection]
    """List of Slack channel connections."""

    token: Optional[Token] = None
    """A Slack connection token."""
