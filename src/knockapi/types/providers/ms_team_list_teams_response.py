# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MsTeamListTeamsResponse", "MsTeamsTeam"]


class MsTeamsTeam(BaseModel):
    id: str

    display_name: str = FieldInfo(alias="displayName")

    description: Optional[str] = None


class MsTeamListTeamsResponse(BaseModel):
    ms_teams_teams: List[MsTeamsTeam]

    skip_token: Optional[str] = None
