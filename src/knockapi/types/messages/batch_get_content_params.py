# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["BatchGetContentParams"]


class BatchGetContentParams(TypedDict, total=False):
    message_ids: Required[Iterable[object]]
    """The IDs of the messages to fetch contents of"""
