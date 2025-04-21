# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..condition_param import ConditionParam

__all__ = ["PreferenceSetChannelTypeSettingParam"]


class PreferenceSetChannelTypeSettingParam(TypedDict, total=False):
    conditions: Required[Iterable[ConditionParam]]
    """A list of conditions to apply to a channel type."""
