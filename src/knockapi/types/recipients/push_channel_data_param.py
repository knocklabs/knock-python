# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["PushChannelDataParam"]


class PushChannelDataParam(TypedDict, total=False):
    tokens: Required[SequenceNotStr[str]]
    """A list of push channel tokens."""
