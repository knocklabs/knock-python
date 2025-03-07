# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.user import User

__all__ = ["AudienceListMembersResponse", "Entry", "PageInfo"]


class Entry(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    added_at: datetime

    user: User
    """A user object"""

    user_id: str

    tenant: Optional[str] = None


class PageInfo(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    page_size: int

    after: Optional[str] = None

    before: Optional[str] = None


class AudienceListMembersResponse(BaseModel):
    entries: List[Entry]

    page_info: PageInfo
    """The information about a paginated result"""
