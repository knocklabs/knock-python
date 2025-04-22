# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OneSignalChannelData"]


class OneSignalChannelData(BaseModel):
    api_typename: Literal["OneSignalChannelData"] = FieldInfo(alias="__typename")
    """The typename of the schema."""

    player_ids: List[str]
    """A list of OneSignal player IDs."""
