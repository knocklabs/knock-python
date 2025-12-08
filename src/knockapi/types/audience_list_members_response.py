# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .audience_member import AudienceMember
from .shared.page_info import PageInfo

__all__ = ["AudienceListMembersResponse"]


class AudienceListMembersResponse(BaseModel):
    """A paginated list of audience members."""

    entries: List[AudienceMember]
    """A list of audience members."""

    page_info: PageInfo
    """Pagination information for a list of resources."""
