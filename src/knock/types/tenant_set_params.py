# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .shared_params.preference_set_request import PreferenceSetRequest
from .shared_params.inline_channel_data_request import InlineChannelDataRequest
from .shared_params.inline_preference_set_request import InlinePreferenceSetRequest

__all__ = ["TenantSetParams", "Settings", "SettingsBranding"]


class TenantSetParams(TypedDict, total=False):
    channel_data: Optional[InlineChannelDataRequest]
    """Allows inline setting channel data for a recipient"""

    preferences: Optional[InlinePreferenceSetRequest]
    """
    Inline set preferences for a recipient, where the key is the preference set name
    """

    settings: Settings


class SettingsBranding(TypedDict, total=False):
    icon_url: Optional[str]

    logo_url: Optional[str]

    primary_color: Optional[str]

    primary_color_contrast: Optional[str]


class Settings(TypedDict, total=False):
    branding: SettingsBranding

    preference_set: Optional[PreferenceSetRequest]
    """Set preferences for a recipient"""
