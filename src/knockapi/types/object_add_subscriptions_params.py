# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .inline_object_request_param import InlineObjectRequestParam
from .inline_identify_user_request_param import InlineIdentifyUserRequestParam

__all__ = ["ObjectAddSubscriptionsParams", "Recipient"]


class ObjectAddSubscriptionsParams(TypedDict, total=False):
    recipients: Required[List[Recipient]]
    """The recipients of the subscription."""

    properties: Optional[Dict[str, object]]
    """The custom properties associated with the recipients of the subscription."""


Recipient: TypeAlias = Union[str, InlineIdentifyUserRequestParam, InlineObjectRequestParam]
