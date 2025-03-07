# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScheduleRepeatRule"]


class ScheduleRepeatRule(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    frequency: Literal["daily", "weekly", "monthly", "hourly"]

    day_of_month: Optional[int] = None

    days: Optional[List[Literal["mon", "tue", "wed", "thu", "fri", "sat", "sun"]]] = None

    hours: Optional[int] = None

    interval: Optional[int] = None

    minutes: Optional[int] = None
