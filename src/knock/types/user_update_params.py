# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.inline_channel_data_request import InlineChannelDataRequest
from .shared_params.inline_preference_set_request import InlinePreferenceSetRequest

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    channel_data: Optional[InlineChannelDataRequest]
    """Allows inline setting channel data for a recipient"""

    created_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    preferences: Optional[InlinePreferenceSetRequest]
    """
    Inline set preferences for a recipient, where the key is the preference set name
    """
