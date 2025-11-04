# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..shared_params.condition import Condition

__all__ = ["PreferenceSetChannelSettingParam"]


class PreferenceSetChannelSettingParam(TypedDict, total=False):
    conditions: Required[Iterable[Condition]]
    """A list of conditions to apply to a specific channel."""
