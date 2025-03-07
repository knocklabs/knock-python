# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "MsTeamsChannelData",
    "Connection",
    "ConnectionMsTeamsTokenConnection",
    "ConnectionMsTeamsIncomingWebhookConnection",
    "ConnectionMsTeamsIncomingWebhookConnectionIncomingWebhook",
]


class ConnectionMsTeamsTokenConnection(TypedDict, total=False):
    ms_teams_channel_id: Optional[str]
    """The Microsoft Teams channel ID"""

    ms_teams_team_id: Optional[str]
    """The Microsoft Teams team ID"""

    ms_teams_tenant_id: Optional[str]
    """The Microsoft Teams tenant ID"""

    ms_teams_user_id: Optional[str]
    """The Microsoft Teams user ID"""


class ConnectionMsTeamsIncomingWebhookConnectionIncomingWebhook(TypedDict, total=False):
    url: Required[str]
    """The URL of the incoming webhook"""


class ConnectionMsTeamsIncomingWebhookConnection(TypedDict, total=False):
    incoming_webhook: Required[ConnectionMsTeamsIncomingWebhookConnectionIncomingWebhook]
    """The incoming webhook"""


Connection: TypeAlias = Union[ConnectionMsTeamsTokenConnection, ConnectionMsTeamsIncomingWebhookConnection]


class MsTeamsChannelData(TypedDict, total=False):
    connections: Required[Iterable[Connection]]

    ms_teams_tenant_id: Optional[str]
    """The Microsoft Teams tenant ID"""
