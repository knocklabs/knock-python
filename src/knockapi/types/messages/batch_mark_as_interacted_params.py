# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["BatchMarkAsInteractedParams"]


class BatchMarkAsInteractedParams(TypedDict, total=False):
    message_ids: Required[List[str]]
    """The message IDs to batch mark as interacted with."""

    metadata: Optional[Dict[str, object]]
    """Metadata about the interaction."""
