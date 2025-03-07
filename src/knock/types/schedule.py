# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .recipient import Recipient
from .schedule_repeat_rule import ScheduleRepeatRule

__all__ = ["Schedule"]


class Schedule(BaseModel):
    id: str

    inserted_at: datetime

    recipient: Recipient
    """A recipient, which is either a user or an object"""

    repeats: List[ScheduleRepeatRule]

    updated_at: datetime

    workflow: str

    api_typename: Optional[str] = FieldInfo(alias="__typename", default=None)

    actor: Optional[Recipient] = None
    """A recipient, which is either a user or an object"""

    data: Optional[Dict[str, object]] = None

    last_occurrence_at: Optional[datetime] = None

    next_occurrence_at: Optional[datetime] = None

    tenant: Optional[str] = None
