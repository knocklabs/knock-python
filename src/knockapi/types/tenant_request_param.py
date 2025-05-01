# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .recipients.preference_set_request_param import PreferenceSetRequestParam
from .recipients.inline_channel_data_request_param import InlineChannelDataRequestParam
from .recipients.inline_preference_set_request_param import InlinePreferenceSetRequestParam

__all__ = ["TenantRequestParam", "Settings", "SettingsBranding"]


class SettingsBranding(TypedDict, total=False):
    icon_url: Optional[str]
    """The icon URL for the tenant.

    Must point to a valid image with an image MIME type.
    """

    logo_url: Optional[str]
    """The logo URL for the tenant.

    Must point to a valid image with an image MIME type.
    """

    primary_color: Optional[str]
    """The primary color for the tenant, provided as a hex value."""

    primary_color_contrast: Optional[str]
    """The primary color contrast for the tenant, provided as a hex value."""


class Settings(TypedDict, total=False):
    branding: SettingsBranding
    """The branding for the tenant."""

    preference_set: Optional[PreferenceSetRequestParam]
    """A request to set a preference set for a recipient."""


class TenantRequestParamTyped(TypedDict, total=False):
    id: Required[str]
    """The unique identifier for the tenant."""

    channel_data: Optional[InlineChannelDataRequestParam]
    """A request to set channel data for a type of channel inline."""

    preferences: Optional[InlinePreferenceSetRequestParam]
    """Inline set preferences for a recipient, where the key is the preference set id."""

    settings: Settings
    """The settings for the tenant. Includes branding and preference set."""


TenantRequestParam: TypeAlias = Union[TenantRequestParamTyped, Dict[str, object]]
