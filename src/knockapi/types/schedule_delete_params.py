# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ScheduleDeleteParams"]


class ScheduleDeleteParams(TypedDict, total=False):
    schedule_ids: Required[List[str]]
    """A list of schedule IDs."""
