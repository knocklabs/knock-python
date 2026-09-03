# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .message import Message
from .._models import BaseModel
from .shared.page_info import PageInfo

__all__ = ["ListMessagesResponse"]


class ListMessagesResponse(BaseModel):
    """A paginated list of messages."""

    items: List[Message]
    """A list of messages."""

    page_info: PageInfo
    """Pagination information for a list of resources."""
