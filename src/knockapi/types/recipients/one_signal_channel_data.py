# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["OneSignalChannelData"]


class OneSignalChannelData(BaseModel):
    player_ids: List[str]
    """A list of OneSignal player IDs."""
