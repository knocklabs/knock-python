# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..shared.condition import Condition

__all__ = ["PreferenceSetChannelSetting"]


class PreferenceSetChannelSetting(BaseModel):
    """A set of settings for a specific channel.

    Currently, this can only be a list of conditions to apply.
    """

    conditions: List[Condition]
    """A list of conditions to apply to a specific channel."""
