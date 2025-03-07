# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Optional
from datetime import datetime

from ..._models import BaseModel
from .inline_channel_data_request import InlineChannelDataRequest
from .inline_preference_set_request import InlinePreferenceSetRequest

__all__ = ["InlineIdentifyUserRequest"]


class InlineIdentifyUserRequest(BaseModel):
    id: str
    """The ID of the user to identify. This is an ID that you supply."""

    channel_data: Optional[InlineChannelDataRequest] = None
    """Allows inline setting channel data for a recipient"""

    created_at: Optional[datetime] = None
    """The creation date of the user from your system."""

    preferences: Optional[InlinePreferenceSetRequest] = None
    """
    Inline set preferences for a recipient, where the key is the preference set name
    """

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
