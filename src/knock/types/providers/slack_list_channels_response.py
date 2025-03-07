# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SlackListChannelsResponse", "SlackChannel"]


class SlackChannel(BaseModel):
    id: str

    context_team_id: str

    is_im: bool

    is_private: bool

    name: str


class SlackListChannelsResponse(BaseModel):
    next_cursor: Optional[str] = None

    slack_channels: List[SlackChannel]
