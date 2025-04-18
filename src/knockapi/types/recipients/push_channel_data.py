# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PushChannelData"]


class PushChannelData(BaseModel):
    api_typename: Literal["PushChannelData"] = FieldInfo(alias="__typename")
    """The typename of the schema."""

    tokens: List[str]
    """A list of push channel tokens."""
