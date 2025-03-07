# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared_params.inline_channel_data_request import InlineChannelDataRequest
from .shared_params.inline_preference_set_request import InlinePreferenceSetRequest

__all__ = ["ObjectSetParams"]


class ObjectSetParams(TypedDict, total=False):
    collection: Required[str]

    channel_data: Optional[InlineChannelDataRequest]
    """Allows inline setting channel data for a recipient"""

    preferences: Optional[InlinePreferenceSetRequest]
    """
    Inline set preferences for a recipient, where the key is the preference set name
    """
