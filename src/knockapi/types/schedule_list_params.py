# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ScheduleListParams"]


class ScheduleListParams(TypedDict, total=False):
    workflow: Required[str]
    """Filter by workflow key."""

    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    page_size: int
    """The number of items per page."""

    recipients: List[str]
    """Filter by recipient IDs."""

    tenant: str
    """Filter by tenant ID."""
