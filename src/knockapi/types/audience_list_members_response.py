# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .audience_member import AudienceMember

__all__ = ["AudienceListMembersResponse", "PageInfo"]


class PageInfo(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    page_size: int

    after: Optional[str] = None

    before: Optional[str] = None


class AudienceListMembersResponse(BaseModel):
    entries: List[AudienceMember]

    page_info: PageInfo
    """The information about a paginated result"""
