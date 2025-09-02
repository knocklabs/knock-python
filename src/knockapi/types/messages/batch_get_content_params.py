# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["BatchGetContentParams"]


class BatchGetContentParams(TypedDict, total=False):
    message_ids: Required[SequenceNotStr[str]]
    """The IDs of the messages to fetch contents of."""
