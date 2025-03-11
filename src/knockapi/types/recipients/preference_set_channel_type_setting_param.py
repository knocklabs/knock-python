# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..shared_params.condition import Condition

__all__ = ["PreferenceSetChannelTypeSettingParam"]


class PreferenceSetChannelTypeSettingParam(TypedDict, total=False):
    conditions: Required[Iterable[Condition]]
