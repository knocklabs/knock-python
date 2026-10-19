# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    include: List[Literal["preferences"]]
    """Associated resources to include in the response."""

    order: Literal["asc", "desc"]
    """Sort by insertion order.

    Pass `asc` for oldest first, or `desc` for newest first. Defaults to oldest
    first when omitted.
    """

    page_size: int
    """The number of items per page (defaults to 50)."""
