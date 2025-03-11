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
    """A set of settings for a channel type.

    Currently, this can only be a list of conditions to apply.
    """

    email: Email
    """A set of settings for a channel type.

    Currently, this can only be a list of conditions to apply.
    """

    http: HTTP
    """A set of settings for a channel type.

    Currently, this can only be a list of conditions to apply.
    """

    in_app_feed: InAppFeed
    """A set of settings for a channel type.

    Currently, this can only be a list of conditions to apply.
    """

    push: Push
    """A set of settings for a channel type.

    Currently, this can only be a list of conditions to apply.
    """

    sms: SMS
    """A set of settings for a channel type.

    Currently, this can only be a list of conditions to apply.
    """
