# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias, TypedDict

from .preference_set_channel_type_setting import PreferenceSetChannelTypeSetting

__all__ = ["PreferenceSetChannelTypes", "Chat", "Email", "HTTP", "InAppFeed", "Push", "SMS"]

Chat: TypeAlias = Union[bool, PreferenceSetChannelTypeSetting]

Email: TypeAlias = Union[bool, PreferenceSetChannelTypeSetting]

HTTP: TypeAlias = Union[bool, PreferenceSetChannelTypeSetting]

InAppFeed: TypeAlias = Union[bool, PreferenceSetChannelTypeSetting]

Push: TypeAlias = Union[bool, PreferenceSetChannelTypeSetting]

SMS: TypeAlias = Union[bool, PreferenceSetChannelTypeSetting]


class PreferenceSetChannelTypes(TypedDict, total=False):
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
