# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SlackListChannelsResponse"]


class SlackListChannelsResponse(BaseModel):
    id: str
    """A Slack channel ID from the Slack provider."""

    context_team_id: str
    """The team ID that the Slack channel belongs to."""

    is_im: bool
    """Whether the Slack channel is an IM channel."""

    is_private: bool
    """Whether the Slack channel is private."""

    name: str
    """Slack channel name."""
