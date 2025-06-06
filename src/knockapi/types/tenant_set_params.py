# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .recipients.preference_set_request_param import PreferenceSetRequestParam
from .recipients.inline_channel_data_request_param import InlineChannelDataRequestParam

__all__ = ["TenantSetParams", "Settings", "SettingsBranding"]


class TenantSetParams(TypedDict, total=False):
    channel_data: Optional[InlineChannelDataRequestParam]
    """A request to set channel data for a type of channel inline."""

    settings: Settings
    """The settings for the tenant. Includes branding and preference set."""


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
