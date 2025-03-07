# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Required, TypedDict

from ..shared_params.recipient_request import RecipientRequest

__all__ = ["BulkAddSubscriptionsParams", "Subscription"]


class BulkAddSubscriptionsParams(TypedDict, total=False):
    subscriptions: Required[Iterable[Subscription]]


class Subscription(TypedDict, total=False):
    id: Required[str]

    recipients: Required[List[RecipientRequest]]

    properties: Optional[Dict[str, object]]
