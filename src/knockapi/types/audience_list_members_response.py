# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .page_info import PageInfo
from .audience_member import AudienceMember

__all__ = ["AudienceListMembersResponse"]


class AudienceListMembersResponse(BaseModel):
    entries: List[AudienceMember]
    """A list of audience members."""

    page_info: PageInfo
    """Pagination information for a list of resources."""
