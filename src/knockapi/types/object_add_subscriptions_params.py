# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .recipient_request_param import RecipientRequestParam

__all__ = ["ObjectAddSubscriptionsParams"]


class ObjectAddSubscriptionsParams(TypedDict, total=False):
    recipients: Required[SequenceNotStr[RecipientRequestParam]]
    """The recipients of the subscription.

    You can subscribe up to 100 recipients to an object at a time.
    """

    properties: Optional[Dict[str, object]]
    """The custom properties associated with the subscription relationship."""
