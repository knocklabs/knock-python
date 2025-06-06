# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ScheduleRepeatRuleParam"]


class ScheduleRepeatRuleParam(TypedDict, total=False):
    frequency: Required[Literal["daily", "weekly", "monthly", "hourly"]]
    """The frequency of the schedule."""

    _typename: Annotated[str, PropertyInfo(alias="__typename")]
    """The typename of the schema."""

    day_of_month: Optional[int]
    """The day of the month to repeat the schedule."""

    days: Optional[List[Literal["mon", "tue", "wed", "thu", "fri", "sat", "sun"]]]
    """The days of the week to repeat the schedule."""

    hours: Optional[int]
    """The hour of the day to repeat the schedule."""

    interval: int
    """The interval of the schedule."""

    minutes: Optional[int]
    """The minute of the hour to repeat the schedule."""
