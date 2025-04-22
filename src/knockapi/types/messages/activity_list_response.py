# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..activity import Activity
from ..page_info import PageInfo

__all__ = ["ActivityListResponse"]


class ActivityListResponse(BaseModel):
    entries: List[Activity]
    """A list of activities."""

    page_info: PageInfo
    """Pagination information for a list of resources."""
