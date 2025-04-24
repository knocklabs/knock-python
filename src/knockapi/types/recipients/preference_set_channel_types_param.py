# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias, TypedDict

from .preference_set_channel_type_setting_param import PreferenceSetChannelTypeSettingParam

__all__ = ["PreferenceSetChannelTypesParam", "Chat", "Email", "HTTP", "InAppFeed", "Push", "SMS"]

Chat: TypeAlias = Union[bool, PreferenceSetChannelTypeSettingParam]

Email: TypeAlias = Union[bool, PreferenceSetChannelTypeSettingParam]

HTTP: TypeAlias = Union[bool, PreferenceSetChannelTypeSettingParam]

InAppFeed: TypeAlias = Union[bool, PreferenceSetChannelTypeSettingParam]

Push: TypeAlias = Union[bool, PreferenceSetChannelTypeSettingParam]

SMS: TypeAlias = Union[bool, PreferenceSetChannelTypeSettingParam]


class PreferenceSetChannelTypesParam(TypedDict, total=False):
    chat: Chat
    """Either a boolean or a setting for the given channel type."""

    email: Email
    """Either a boolean or a setting for the given channel type."""

    http: HTTP
    """Either a boolean or a setting for the given channel type."""

    in_app_feed: InAppFeed
    """Either a boolean or a setting for the given channel type."""

    push: Push
    """Either a boolean or a setting for the given channel type."""

    sms: SMS
    """Either a boolean or a setting for the given channel type."""
