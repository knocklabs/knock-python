# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .inline_object_request_param import InlineObjectRequestParam
from .inline_identify_user_request_param import InlineIdentifyUserRequestParam

__all__ = ["RecipientRequestParam"]

RecipientRequestParam: TypeAlias = Union[str, InlineIdentifyUserRequestParam, InlineObjectRequestParam]
