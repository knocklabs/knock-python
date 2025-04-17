# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MsTeamListChannelsResponse", "MsTeamsChannel"]


class MsTeamsChannel(BaseModel):
    id: str
    """Microsoft Teams channel ID."""

    display_name: str = FieldInfo(alias="displayName")
    """Microsoft Teams channel name."""

    created_date_time: Optional[str] = FieldInfo(alias="createdDateTime", default=None)
    """Microsoft Teams channel created date and time."""

    description: Optional[str] = None
    """Microsoft Teams channel description."""

    is_archived: Optional[bool] = FieldInfo(alias="isArchived", default=None)
    """Whether the Microsoft Teams channel is archived."""

    membership_type: Optional[str] = FieldInfo(alias="membershipType", default=None)
    """Microsoft Teams channel membership type."""


class MsTeamListChannelsResponse(BaseModel):
    ms_teams_channels: List[MsTeamsChannel]
    """List of Microsoft Teams channels."""
