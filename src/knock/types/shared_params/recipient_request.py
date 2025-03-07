# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .inline_object_request import InlineObjectRequest
from .inline_identify_user_request import InlineIdentifyUserRequest

__all__ = ["RecipientRequest"]

RecipientRequest: TypeAlias = Union[str, InlineIdentifyUserRequest, InlineObjectRequest]
