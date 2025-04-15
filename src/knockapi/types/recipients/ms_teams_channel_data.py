# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["MsTeamsChannelData", "Connection", "ConnectionTokenConnection", "ConnectionIncomingWebhookConnection"]


class ConnectionTokenConnection(BaseModel):
    access_token: Optional[str] = None

    channel_id: Optional[str] = None

    user_id: Optional[str] = None


class ConnectionIncomingWebhookConnection(BaseModel):
    url: str


Connection: TypeAlias = Union[ConnectionTokenConnection, ConnectionIncomingWebhookConnection]


class MsTeamsChannelData(BaseModel):
    connections: List[Connection]

    ms_teams_tenant_id: Optional[str] = None
    """The Microsoft Teams tenant ID"""
