# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .recipient_reference_param import RecipientReferenceParam

__all__ = ["ObjectDeleteSubscriptionsParams"]


class ObjectDeleteSubscriptionsParams(TypedDict, total=False):
    recipients: Required[List[RecipientReferenceParam]]
    """The recipients of the subscription.

    You can subscribe up to 100 recipients to an object at a time.
    """
