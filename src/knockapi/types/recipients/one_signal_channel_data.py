# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OneSignalChannelData"]


class OneSignalChannelData(BaseModel):
    player_ids: List[str]
    """A list of OneSignal player IDs."""

    type: Literal["push_one_signal"]
    """The type of provider."""

    api_typename: Optional[Literal["OneSignalChannelData"]] = FieldInfo(alias="__typename", default=None)
    """The typename of the schema."""
