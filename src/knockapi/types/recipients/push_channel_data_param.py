# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["PushChannelDataParam"]


class PushChannelDataParam(TypedDict, total=False):
    tokens: Required[List[str]]
    """A list of push channel tokens."""
