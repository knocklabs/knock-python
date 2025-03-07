# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ObjectListSubscriptionsParams", "Recipient", "RecipientObjectReference"]


class ObjectListSubscriptionsParams(TypedDict, total=False):
    collection: Required[str]

    after: str
    """The cursor to fetch entries after"""

    before: str
    """The cursor to fetch entries before"""

    mode: Literal["recipient", "object"]
    """Mode of the request"""

    page_size: int
    """The page size to fetch"""

    recipients: List[Recipient]
    """Recipients to filter by (only used if mode is `object`)"""


class RecipientObjectReference(TypedDict, total=False):
    id: Required[str]
    """An object identifier"""

    collection: Required[str]
    """The collection the object belongs to"""


Recipient: TypeAlias = Union[str, RecipientObjectReference]
