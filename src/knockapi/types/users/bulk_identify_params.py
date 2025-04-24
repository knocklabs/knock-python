# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["BulkIdentifyParams"]


class BulkIdentifyParams(TypedDict, total=False):
    users: Required[Iterable["InlineIdentifyUserRequestParam"]]
    """A list of users."""


from ..inline_identify_user_request_param import InlineIdentifyUserRequestParam
