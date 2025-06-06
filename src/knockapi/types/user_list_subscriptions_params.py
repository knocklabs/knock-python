# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .recipient_reference_param import RecipientReferenceParam

__all__ = ["UserListSubscriptionsParams"]


class UserListSubscriptionsParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    include: List[Literal["preferences"]]
    """Associated resources to include in the response."""

    objects: List[RecipientReferenceParam]
    """Only returns subscriptions for the specified object references."""

    page_size: int
    """The number of items per page."""
