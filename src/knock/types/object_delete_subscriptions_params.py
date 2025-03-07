# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .shared_params.recipient_request import RecipientRequest

__all__ = ["ObjectDeleteSubscriptionsParams"]


class ObjectDeleteSubscriptionsParams(TypedDict, total=False):
    collection: Required[str]

    recipients: Required[List[RecipientRequest]]
