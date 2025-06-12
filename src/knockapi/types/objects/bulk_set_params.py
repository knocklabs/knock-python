# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from ..recipients.inline_channel_data_request_param import InlineChannelDataRequestParam
from ..recipients.inline_preference_set_request_param import InlinePreferenceSetRequestParam

__all__ = ["BulkSetParams", "Object"]


class BulkSetParams(TypedDict, total=False):
    objects: Required[Iterable[Object]]
    """A list of objects."""


class ObjectTyped(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the object."""

    channel_data: Optional[InlineChannelDataRequestParam]
    """A request to set channel data for a type of channel inline."""

    created_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Timestamp when the resource was created."""

    preferences: Optional[InlinePreferenceSetRequestParam]
    """Inline set preferences for a recipient, where the key is the preference set id.

    Preferences that are set inline will be merged into any existing preferences
    rather than replacing them.
    """


Object: TypeAlias = Union[ObjectTyped, Dict[str, object]]
