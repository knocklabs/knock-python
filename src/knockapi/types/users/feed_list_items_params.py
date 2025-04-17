# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["FeedListItemsParams"]


class FeedListItemsParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after."""

    archived: Literal["exclude", "include", "only"]
    """The archived status of the feed items."""

    before: str
    """The cursor to fetch entries before."""

    has_tenant: bool
    """Whether the feed items have a tenant."""

    page_size: int
    """The number of items per page."""

    source: str
    """The source of the feed items."""

    status: Literal["unread", "read", "unseen", "seen", "all"]
    """The status of the feed items."""

    tenant: str
    """The tenant associated with the feed items."""

    trigger_data: str
    """The trigger data of the feed items (as a JSON string)."""

    workflow_categories: List[str]
    """The workflow categories of the feed items."""
