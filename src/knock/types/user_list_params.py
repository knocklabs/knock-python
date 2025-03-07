# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after"""

    before: str
    """The cursor to fetch entries before"""

    page_size: int
    """The page size to fetch"""
