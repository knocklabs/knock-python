# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["UserListSubscriptionsParams", "Object", "ObjectUnionMember1"]


class UserListSubscriptionsParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after"""

    before: str
    """The cursor to fetch entries before"""

    objects: List[Object]
    """Objects to filter by"""

    page_size: int
    """The page size to fetch"""


class ObjectUnionMember1(TypedDict, total=False):
    id: Required[str]
    """An object identifier"""

    collection: Required[str]
    """The collection the object belongs to"""


Object: TypeAlias = Union[str, ObjectUnionMember1]
