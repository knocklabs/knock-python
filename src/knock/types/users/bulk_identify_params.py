# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..shared_params.inline_identify_user_request import InlineIdentifyUserRequest

__all__ = ["BulkIdentifyParams"]


class BulkIdentifyParams(TypedDict, total=False):
    users: Required[Iterable[InlineIdentifyUserRequest]]
