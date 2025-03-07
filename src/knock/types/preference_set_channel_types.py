# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
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
    """A set of settings for a channel type.

    Currently, this can only be a list of conditions to apply.
    """

    email: Optional[Email] = None
    """A set of settings for a channel type.

    Currently, this can only be a list of conditions to apply.
    """

    http: Optional[HTTP] = None
    """A set of settings for a channel type.

    Currently, this can only be a list of conditions to apply.
    """

    in_app_feed: Optional[InAppFeed] = None
    """A set of settings for a channel type.

    Currently, this can only be a list of conditions to apply.
    """

    push: Optional[Push] = None
    """A set of settings for a channel type.

    Currently, this can only be a list of conditions to apply.
    """

    sms: Optional[SMS] = None
    """A set of settings for a channel type.

    Currently, this can only be a list of conditions to apply.
    """
