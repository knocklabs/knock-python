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

    logo_url: Optional[str]

    primary_color: Optional[str]

    primary_color_contrast: Optional[str]


class Settings(TypedDict, total=False):
    branding: SettingsBranding

    preference_set: Optional[PreferenceSetRequestParam]
    """Set preferences for a recipient"""


class TenantRequestParamTyped(TypedDict, total=False):
    id: Required[str]

    channel_data: Optional[InlineChannelDataRequestParam]
    """Allows inline setting channel data for a recipient"""

    preferences: Optional[InlinePreferenceSetRequestParam]
    """
    Inline set preferences for a recipient, where the key is the preference set name
    """

    settings: Settings


TenantRequestParam: TypeAlias = Union[TenantRequestParamTyped, Dict[str, object]]
