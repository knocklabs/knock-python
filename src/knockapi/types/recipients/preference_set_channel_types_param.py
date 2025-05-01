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
    """Whether the channel type is enabled for the preference set."""

    email: Email
    """Whether the channel type is enabled for the preference set."""

    http: HTTP
    """Whether the channel type is enabled for the preference set."""

    in_app_feed: InAppFeed
    """Whether the channel type is enabled for the preference set."""

    push: Push
    """Whether the channel type is enabled for the preference set."""

    sms: SMS
    """Whether the channel type is enabled for the preference set."""
