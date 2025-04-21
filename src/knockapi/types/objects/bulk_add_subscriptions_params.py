# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from ..inline_object_request_param import InlineObjectRequestParam
from ..inline_identify_user_request_param import InlineIdentifyUserRequestParam

__all__ = ["BulkAddSubscriptionsParams", "Subscription", "SubscriptionRecipient"]


class BulkAddSubscriptionsParams(TypedDict, total=False):
    subscriptions: Required[Iterable[Subscription]]
    """A list of subscriptions."""


SubscriptionRecipient: TypeAlias = Union[str, InlineIdentifyUserRequestParam, InlineObjectRequestParam]


class Subscription(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the subscription."""

    recipients: Required[List[SubscriptionRecipient]]
    """The recipients of the subscription."""

    properties: Optional[Dict[str, object]]
    """The custom properties associated with the recipients of the subscription."""
