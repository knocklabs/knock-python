# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserListSchedulesParams"]


class UserListSchedulesParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    page_size: int
    """The number of items per page."""

    tenant: str
    """The tenant ID to filter schedules for."""

    workflow: str
    """The workflow key to filter schedules for."""
