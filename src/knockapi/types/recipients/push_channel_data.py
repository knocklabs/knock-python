# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["PushChannelData"]


class PushChannelData(BaseModel):
    tokens: List[str]
    """A list of push channel tokens."""
