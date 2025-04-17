# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MsTeamCheckAuthResponse", "Connection"]


class Connection(BaseModel):
    ok: bool
    """Whether the Microsoft Teams connection is valid."""

    reason: Optional[str] = None
    """The reason for the Microsoft Teams connection if it is not valid."""


class MsTeamCheckAuthResponse(BaseModel):
    connection: Connection
    """A Microsoft Teams connection object."""
