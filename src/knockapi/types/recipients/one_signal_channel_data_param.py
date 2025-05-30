# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["OneSignalChannelDataParam"]


class OneSignalChannelDataParam(TypedDict, total=False):
    player_ids: Required[List[str]]
    """A list of OneSignal player IDs."""
