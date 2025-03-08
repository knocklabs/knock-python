# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Required, TypedDict

from .recipient_request_param import RecipientRequestParam

__all__ = ["ObjectAddSubscriptionsParams"]


class ObjectAddSubscriptionsParams(TypedDict, total=False):
    recipients: Required[List[RecipientRequestParam]]
    """The recipients to subscribe to the object"""

    properties: Optional[Dict[str, object]]
    """The custom properties associated with the subscription"""
