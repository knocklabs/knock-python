# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PushChannelData"]


class PushChannelData(BaseModel):
    tokens: List[str]
    """A list of push channel tokens."""

    type: Literal["push_fcm", "push_apns", "push_expo"]
    """The type of provider."""

    api_typename: Optional[Literal["PushChannelData"]] = FieldInfo(alias="__typename", default=None)
    """The typename of the schema."""
