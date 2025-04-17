# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SlackCheckAuthResponse", "Connection"]


class Connection(BaseModel):
    ok: bool
    """Whether the Slack connection is valid."""

    reason: Optional[str] = None
    """The reason for the Slack connection if it is not valid."""


class SlackCheckAuthResponse(BaseModel):
    connection: Connection
    """A Slack connection object."""
