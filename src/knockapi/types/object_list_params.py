# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ObjectListParams"]


class ObjectListParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    include: List[Literal["preferences"]]
    """Includes preferences of the objects in the response."""

    page_size: int
    """The number of items per page."""
