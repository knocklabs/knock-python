# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OneSignalChannelDataParam"]


class OneSignalChannelDataParam(TypedDict, total=False):
    _typename: Required[Annotated[Literal["OneSignalChannelData"], PropertyInfo(alias="__typename")]]
    """The typename of the schema."""

    player_ids: Required[List[str]]
    """A list of OneSignal player IDs."""

    type: Required[Literal["push_one_signal"]]
    """The channel type identifier"""
