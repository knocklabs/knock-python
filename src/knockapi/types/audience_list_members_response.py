# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .audience_member import AudienceMember

__all__ = ["AudienceListMembersResponse", "PageInfo"]


class PageInfo(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")
    """The type name of the schema."""

    page_size: int
    """The number of items per page."""

    after: Optional[str] = None
    """The cursor to fetch entries after."""

    before: Optional[str] = None
    """The cursor to fetch entries before."""


class AudienceListMembersResponse(BaseModel):
    entries: List[AudienceMember]
    """A list of audience members."""

    page_info: PageInfo
    """Pagination information for a list of resources."""
