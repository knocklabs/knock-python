# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MsTeamCheckAuthResponse", "Connection"]


class Connection(BaseModel):
    """A Microsoft Teams connection object."""

    ok: bool
    """Whether the Microsoft Teams connection is valid."""

    reason: Optional[str] = None
    """The reason for the Microsoft Teams connection if it is not valid."""


class MsTeamCheckAuthResponse(BaseModel):
    """The response from a Microsoft Teams auth check request."""

    connection: Connection
    """A Microsoft Teams connection object."""
