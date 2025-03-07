# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BulkDeleteParams"]


class BulkDeleteParams(TypedDict, total=False):
    query_user_ids: Required[Annotated[List[str], PropertyInfo(alias="user_ids")]]
    """The IDs of the users to delete"""

    body_user_ids: Required[Annotated[List[str], PropertyInfo(alias="user_ids")]]
