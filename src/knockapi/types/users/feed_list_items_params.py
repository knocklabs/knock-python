# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["FeedListItemsParams"]


class FeedListItemsParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after"""

    archived: Literal["exclude", "include", "only"]
    """The archived status of the feed items to return"""

    before: str
    """The cursor to fetch entries before"""

    has_tenant: bool
    """Whether the feed items have a tenant"""

    page_size: int
    """The page size to fetch"""

    source: str
    """The source of the feed items to return"""

    status: Literal["unread", "read", "unseen", "seen", "all"]
    """The status of the feed items to return"""

    tenant: str
    """The tenant of the feed items to return"""

    trigger_data: str
    """The trigger data of the feed items to return (as a JSON string)"""

    workflow_categories: List[str]
    """The workflow categories of the feed items to return"""
