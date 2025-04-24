# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .recipients.inline_channel_data_request_param import InlineChannelDataRequestParam
from .recipients.inline_preference_set_request_param import InlinePreferenceSetRequestParam

__all__ = ["InlineObjectRequestParam"]


class InlineObjectRequestParamTyped(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the object."""

    collection: Required[str]
    """The collection this object belongs to."""

    channel_data: Optional[InlineChannelDataRequestParam]
    """A request to set channel data for a type of channel inline."""

    created_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Timestamp when the resource was created."""

    preferences: Optional[InlinePreferenceSetRequestParam]
    """Inline set preferences for a recipient, where the key is the preference set id."""


InlineObjectRequestParam: TypeAlias = Union[InlineObjectRequestParamTyped, Dict[str, object]]
