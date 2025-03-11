# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .recipients.inline_channel_data_request_param import InlineChannelDataRequestParam
from .recipients.inline_preference_set_request_param import InlinePreferenceSetRequestParam

__all__ = ["InlineIdentifyUserRequestParam"]


class InlineIdentifyUserRequestParamTyped(TypedDict, total=False):
    id: Required[str]
    """The ID of the user to identify. This is an ID that you supply."""

    channel_data: Optional[InlineChannelDataRequestParam]
    """Allows inline setting channel data for a recipient"""

    created_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The creation date of the user from your system."""

    preferences: Optional[InlinePreferenceSetRequestParam]
    """
    Inline set preferences for a recipient, where the key is the preference set name
    """


InlineIdentifyUserRequestParam: TypeAlias = Union[InlineIdentifyUserRequestParamTyped, Dict[str, object]]
