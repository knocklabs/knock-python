# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GuideGetChannelParams"]


class GuideGetChannelParams(TypedDict, total=False):
    data: str
    """The data to filter guides by."""

    tenant: str
    """The tenant ID to filter guides by."""

    type: str
    """The type of guides to filter by."""
