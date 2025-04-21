# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..condition import Condition

__all__ = ["PreferenceSetChannelTypeSetting"]


class PreferenceSetChannelTypeSetting(BaseModel):
    conditions: List[Condition]
    """A list of conditions to apply to a channel type."""
