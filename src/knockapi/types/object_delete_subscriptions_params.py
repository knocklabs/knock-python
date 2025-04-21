# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypeAlias, TypedDict

from .inline_object_request_param import InlineObjectRequestParam
from .inline_identify_user_request_param import InlineIdentifyUserRequestParam

__all__ = ["ObjectDeleteSubscriptionsParams", "Recipient"]


class ObjectDeleteSubscriptionsParams(TypedDict, total=False):
    recipients: Required[List[Recipient]]
    """The recipients of the subscription."""


Recipient: TypeAlias = Union[str, InlineIdentifyUserRequestParam, InlineObjectRequestParam]
