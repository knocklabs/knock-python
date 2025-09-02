# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .recipient_reference_param import RecipientReferenceParam

__all__ = ["ObjectDeleteSubscriptionsParams"]


class ObjectDeleteSubscriptionsParams(TypedDict, total=False):
    recipients: Required[SequenceNotStr[RecipientReferenceParam]]
    """The recipients of the subscription.

    You can subscribe up to 100 recipients to an object at a time.
    """
