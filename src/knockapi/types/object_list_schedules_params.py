# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ObjectListSchedulesParams"]


class ObjectListSchedulesParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    page_size: int
    """The number of items per page."""

    tenant: str
    """Filter schedules by tenant id."""

    workflow: str
    """Filter schedules by workflow id."""
