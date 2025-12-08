# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from ..recipient_reference_param import RecipientReferenceParam

__all__ = ["BulkDeleteSubscriptionsParams", "Subscription"]


class BulkDeleteSubscriptionsParams(TypedDict, total=False):
    subscriptions: Required[Iterable[Subscription]]
    """A nested list of subscriptions."""


class Subscription(TypedDict, total=False):
    """A list of subscriptions. 1 subscribed-to id, and N subscriber recipients."""

    id: Required[str]
    """Unique identifier for the object."""

    recipients: Required[SequenceNotStr[RecipientReferenceParam]]
    """The recipients of the subscription.

    You can subscribe up to 100 recipients to an object at a time.
    """
