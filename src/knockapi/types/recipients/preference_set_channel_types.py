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
    """Either a boolean or a setting for the given channel type."""

    email: Optional[Email] = None
    """Either a boolean or a setting for the given channel type."""

    http: Optional[HTTP] = None
    """Either a boolean or a setting for the given channel type."""

    in_app_feed: Optional[InAppFeed] = None
    """Either a boolean or a setting for the given channel type."""

    push: Optional[Push] = None
    """Either a boolean or a setting for the given channel type."""

    sms: Optional[SMS] = None
    """Either a boolean or a setting for the given channel type."""
