# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ScheduleRepeatRule"]


class ScheduleRepeatRule(BaseModel):
    frequency: Literal["daily", "weekly", "monthly", "hourly"]
    """The frequency of the schedule."""

    api_typename: Optional[str] = FieldInfo(alias="__typename", default=None)
    """The typename of the schema."""

    day_of_month: Optional[int] = None
    """The day of the month to repeat the schedule."""

    days: Optional[List[Literal["mon", "tue", "wed", "thu", "fri", "sat", "sun"]]] = None
    """The days of the week to repeat the schedule."""

    hours: Optional[int] = None
    """The hour of the day to repeat the schedule."""

    interval: Optional[int] = None
    """The interval of the schedule."""

    minutes: Optional[int] = None
    """The minute of the hour to repeat the schedule."""
