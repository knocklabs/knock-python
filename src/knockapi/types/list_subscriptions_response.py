# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.page_info import PageInfo
from .recipients.subscription import Subscription

__all__ = ["ListSubscriptionsResponse"]


class ListSubscriptionsResponse(BaseModel):
    """A response containing a list of subscriptions."""

    entries: List[Subscription]
    """A list of subscriptions."""

    page_info: PageInfo
    """Pagination information for a list of resources."""
