# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PageInfo"]


class PageInfo(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    page_size: int
    """The number of items per page."""

    after: Optional[str] = None
    """The cursor to fetch entries after."""

    before: Optional[str] = None
    """The cursor to fetch entries before."""
