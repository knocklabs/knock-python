# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ObjectListSchedulesParams"]


class ObjectListSchedulesParams(TypedDict, total=False):
    collection: Required[str]

    after: str
    """The cursor to fetch entries after"""

    before: str
    """The cursor to fetch entries before"""

    page_size: int
    """The page size to fetch"""

    tenant: str
    """The ID of the tenant to list schedules for"""

    workflow: str
    """The ID of the workflow to list schedules for"""
