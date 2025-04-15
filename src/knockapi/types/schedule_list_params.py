# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["ScheduleListParams", "Recipient", "RecipientUnionMember1"]


class ScheduleListParams(TypedDict, total=False):
    workflow: Required[str]
    """Filter by workflow"""

    after: str
    """The cursor to fetch entries after"""

    before: str
    """The cursor to fetch entries before"""

    page_size: int
    """The page size to fetch"""

    recipients: List[Recipient]
    """Filter by recipient"""

    tenant: str
    """Filter by tenant"""


class RecipientUnionMember1(TypedDict, total=False):
    id: Required[str]
    """An object identifier"""

    collection: Required[str]
    """The collection the object belongs to"""


Recipient: TypeAlias = Union[str, RecipientUnionMember1]
