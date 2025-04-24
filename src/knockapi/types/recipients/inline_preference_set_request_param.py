# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List
from typing_extensions import TypeAlias, TypeAliasType

from ..._compat import PYDANTIC_V2

__all__ = ["InlinePreferenceSetRequestParam"]

if TYPE_CHECKING or PYDANTIC_V2:
    InlinePreferenceSetRequestParam = TypeAliasType(
        "InlinePreferenceSetRequestParam", List["inline_preference_set_request_param.InlinePreferenceSetRequestParam"]
    )
else:
    InlinePreferenceSetRequestParam: TypeAlias = List[
        "inline_preference_set_request_param.InlinePreferenceSetRequestParam"
    ]

from . import inline_preference_set_request_param
