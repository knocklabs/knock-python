# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MsTeamListTeamsResponse"]


class MsTeamListTeamsResponse(BaseModel):
    id: str
    """Microsoft Teams team ID."""

    display_name: str = FieldInfo(alias="displayName")
    """Microsoft Teams team display name."""

    description: Optional[str] = None
    """Microsoft Teams team description."""
