# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "MsTeamsChannelData",
    "Connection",
    "ConnectionMsTeamsTokenConnection",
    "ConnectionMsTeamsIncomingWebhookConnection",
    "ConnectionMsTeamsIncomingWebhookConnectionIncomingWebhook",
]


class ConnectionMsTeamsTokenConnection(BaseModel):
    ms_teams_channel_id: Optional[str] = None
    """Microsoft Teams channel ID."""

    ms_teams_team_id: Optional[str] = None
    """Microsoft Teams team ID."""

    ms_teams_tenant_id: Optional[str] = None
    """Microsoft Teams tenant ID."""

    ms_teams_user_id: Optional[str] = None
    """Microsoft Teams user ID."""


class ConnectionMsTeamsIncomingWebhookConnectionIncomingWebhook(BaseModel):
    url: str
    """Microsoft Teams incoming webhook URL."""


class ConnectionMsTeamsIncomingWebhookConnection(BaseModel):
    incoming_webhook: ConnectionMsTeamsIncomingWebhookConnectionIncomingWebhook
    """Microsoft Teams incoming webhook."""


Connection: TypeAlias = Union[ConnectionMsTeamsTokenConnection, ConnectionMsTeamsIncomingWebhookConnection]


class MsTeamsChannelData(BaseModel):
    connections: List[Connection]
    """List of Microsoft Teams connections."""

    ms_teams_tenant_id: Optional[str] = None
    """Microsoft Teams tenant ID."""
