# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["BatchArchiveParams"]


class BatchArchiveParams(TypedDict, total=False):
    message_ids: Required[SequenceNotStr[str]]
    """The message IDs to update the status of."""
