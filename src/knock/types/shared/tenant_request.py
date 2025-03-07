# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Optional

from ..._models import BaseModel
from .preference_set_request import PreferenceSetRequest
from .inline_channel_data_request import InlineChannelDataRequest
from .inline_preference_set_request import InlinePreferenceSetRequest

__all__ = ["TenantRequest", "Settings", "SettingsBranding"]


class SettingsBranding(BaseModel):
    icon_url: Optional[str] = None

    logo_url: Optional[str] = None

    primary_color: Optional[str] = None

    primary_color_contrast: Optional[str] = None


class Settings(BaseModel):
    branding: Optional[SettingsBranding] = None

    preference_set: Optional[PreferenceSetRequest] = None
    """Set preferences for a recipient"""


class TenantRequest(BaseModel):
    id: str

    channel_data: Optional[InlineChannelDataRequest] = None
    """Allows inline setting channel data for a recipient"""

    preferences: Optional[InlinePreferenceSetRequest] = None
    """
    Inline set preferences for a recipient, where the key is the preference set name
    """

    settings: Optional[Settings] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
