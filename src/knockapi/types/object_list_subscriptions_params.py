# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .recipient_reference_param import RecipientReferenceParam

__all__ = ["ObjectListSubscriptionsParams"]


class ObjectListSubscriptionsParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    include: List[Literal["preferences"]]
    """Additional fields to include in the response."""

    mode: Literal["recipient", "object"]
    """Mode of the request."""

    objects: List[RecipientReferenceParam]
    """Objects to filter by (only used if mode is `recipient`)."""

    page_size: int
    """The number of items per page."""

    recipients: List[RecipientReferenceParam]
    """Recipients to filter by (only used if mode is `object`)."""
