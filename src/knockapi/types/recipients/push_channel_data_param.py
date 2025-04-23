# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PushChannelDataParam"]


class PushChannelDataParam(TypedDict, total=False):
    _typename: Required[Annotated[Literal["PushChannelData"], PropertyInfo(alias="__typename")]]
    """The typename of the schema."""

    tokens: Required[List[str]]
    """A list of push channel tokens."""

    type: Required[Literal["push_fcm", "push_apns", "push_expo"]]
    """The push provider type"""
