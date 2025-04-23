# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "MsTeamsChannelDataParam",
    "Connection",
    "ConnectionMsTeamsTokenConnection",
    "ConnectionMsTeamsIncomingWebhookConnection",
    "ConnectionMsTeamsIncomingWebhookConnectionIncomingWebhook",
]


class ConnectionMsTeamsTokenConnection(TypedDict, total=False):
    ms_teams_channel_id: Optional[str]
    """Microsoft Teams channel ID."""

    ms_teams_team_id: Optional[str]
    """Microsoft Teams team ID."""

    ms_teams_tenant_id: Optional[str]
    """Microsoft Teams tenant ID."""

    ms_teams_user_id: Optional[str]
    """Microsoft Teams user ID."""


class ConnectionMsTeamsIncomingWebhookConnectionIncomingWebhook(TypedDict, total=False):
    url: Required[str]
    """Microsoft Teams incoming webhook URL."""


class ConnectionMsTeamsIncomingWebhookConnection(TypedDict, total=False):
    incoming_webhook: Required[ConnectionMsTeamsIncomingWebhookConnectionIncomingWebhook]
    """Microsoft Teams incoming webhook."""


Connection: TypeAlias = Union[ConnectionMsTeamsTokenConnection, ConnectionMsTeamsIncomingWebhookConnection]


class MsTeamsChannelDataParam(TypedDict, total=False):
    _typename: Required[Annotated[Literal["MsTeamsChannelData"], PropertyInfo(alias="__typename")]]
    """The typename of the schema."""

    connections: Required[Iterable[Connection]]
    """List of Microsoft Teams connections."""

    type: Required[Literal["chat_ms_teams"]]
    """The channel type identifier"""

    ms_teams_tenant_id: Optional[str]
    """Microsoft Teams tenant ID."""
