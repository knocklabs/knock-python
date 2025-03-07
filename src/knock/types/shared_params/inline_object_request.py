# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .inline_channel_data_request import InlineChannelDataRequest
from .inline_preference_set_request import InlinePreferenceSetRequest

__all__ = ["InlineObjectRequest"]


class InlineObjectRequestTyped(TypedDict, total=False):
    id: Required[str]

    collection: Required[str]

    channel_data: Optional[InlineChannelDataRequest]
    """Allows inline setting channel data for a recipient"""

    created_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    preferences: Optional[InlinePreferenceSetRequest]
    """
    Inline set preferences for a recipient, where the key is the preference set name
    """


InlineObjectRequest: TypeAlias = Union[InlineObjectRequestTyped, Dict[str, object]]
