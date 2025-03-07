# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ScheduleRepeatRule"]


class ScheduleRepeatRule(TypedDict, total=False):
    _typename: Required[Annotated[str, PropertyInfo(alias="__typename")]]

    frequency: Required[Literal["daily", "weekly", "monthly", "hourly"]]

    day_of_month: Optional[int]

    days: Optional[List[Literal["mon", "tue", "wed", "thu", "fri", "sat", "sun"]]]

    hours: Optional[int]

    interval: int

    minutes: Optional[int]
