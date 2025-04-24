# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .preference_set_channel_type_setting import PreferenceSetChannelTypeSetting

__all__ = ["PreferenceSetChannelTypes", "Chat", "Email", "HTTP", "InAppFeed", "Push", "SMS"]

Chat: TypeAlias = Union[bool, PreferenceSetChannelTypeSetting]

Email: TypeAlias = Union[bool, PreferenceSetChannelTypeSetting]

HTTP: TypeAlias = Union[bool, PreferenceSetChannelTypeSetting]

InAppFeed: TypeAlias = Union[bool, PreferenceSetChannelTypeSetting]

Push: TypeAlias = Union[bool, PreferenceSetChannelTypeSetting]

SMS: TypeAlias = Union[bool, PreferenceSetChannelTypeSetting]


class PreferenceSetChannelTypes(BaseModel):
    chat: Optional[Chat] = None
    """Whether the channel type is enabled for the preference set."""

    email: Optional[Email] = None
    """Whether the channel type is enabled for the preference set."""

    http: Optional[HTTP] = None
    """Whether the channel type is enabled for the preference set."""

    in_app_feed: Optional[InAppFeed] = None
    """Whether the channel type is enabled for the preference set."""

    push: Optional[Push] = None
    """Whether the channel type is enabled for the preference set."""

    sms: Optional[SMS] = None
    """Whether the channel type is enabled for the preference set."""
