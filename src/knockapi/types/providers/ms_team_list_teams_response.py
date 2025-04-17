# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MsTeamListTeamsResponse", "MsTeamsTeam"]


class MsTeamsTeam(BaseModel):
    id: str
    """Microsoft Teams team ID."""

    display_name: str = FieldInfo(alias="displayName")
    """Microsoft Teams team display name."""

    description: Optional[str] = None
    """Microsoft Teams team description."""


class MsTeamListTeamsResponse(BaseModel):
    ms_teams_teams: List[MsTeamsTeam]
    """List of Microsoft Teams teams."""

    skip_token: Optional[str] = None
    """
    [OData param](https://learn.microsoft.com/en-us/graph/query-parameters) passed
    to the Microsoft Graph API to retrieve the next page of results.
    """
