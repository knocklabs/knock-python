# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .schedule import Schedule
from .shared.page_info import PageInfo

__all__ = ["ListSchedulesResponse"]


class ListSchedulesResponse(BaseModel):
    """A response containing a list of schedules."""

    entries: List[Schedule]
    """A list of schedules."""

    page_info: PageInfo
    """Pagination information for a list of resources."""
