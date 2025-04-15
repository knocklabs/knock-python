# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ObjectListSubscriptionsParams", "Object", "ObjectUnionMember1", "Recipient", "RecipientUnionMember1"]


class ObjectListSubscriptionsParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after"""

    before: str
    """The cursor to fetch entries before"""

    mode: Literal["recipient", "object"]
    """Mode of the request"""

    objects: List[Object]
    """Objects to filter by (only used if mode is `recipient`)"""

    page_size: int
    """The page size to fetch"""

    recipients: List[Recipient]
    """Recipients to filter by (only used if mode is `object`)"""


class ObjectUnionMember1(TypedDict, total=False):
    id: Required[str]
    """An object identifier"""

    collection: Required[str]
    """The collection the object belongs to"""


Object: TypeAlias = Union[str, ObjectUnionMember1]


class RecipientUnionMember1(TypedDict, total=False):
    id: Required[str]
    """An object identifier"""

    collection: Required[str]
    """The collection the object belongs to"""


Recipient: TypeAlias = Union[str, RecipientUnionMember1]
