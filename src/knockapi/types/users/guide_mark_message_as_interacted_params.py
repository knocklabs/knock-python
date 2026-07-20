# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["GuideMarkMessageAsInteractedParams"]


class GuideMarkMessageAsInteractedParams(TypedDict, total=False):
    channel_id: Required[str]
    """The unique identifier for the channel."""

    guide_id: Required[str]
    """The unique identifier for the guide."""

    guide_key: Required[str]
    """The key of the guide."""

    guide_step_ref: Required[str]
    """The step reference of the guide."""

    metadata: Dict[str, object]
    """Metadata about the interaction."""

    tenant: str
    """The tenant ID of the guide."""
