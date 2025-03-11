# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MsTeamListChannelsResponse", "MsTeamsChannel"]


class MsTeamsChannel(BaseModel):
    id: str

    display_name: str = FieldInfo(alias="displayName")

    created_date_time: Optional[str] = FieldInfo(alias="createdDateTime", default=None)

    description: Optional[str] = None

    is_archived: Optional[bool] = FieldInfo(alias="isArchived", default=None)

    membership_type: Optional[str] = FieldInfo(alias="membershipType", default=None)


class MsTeamListChannelsResponse(BaseModel):
    ms_teams_channels: List[MsTeamsChannel]
