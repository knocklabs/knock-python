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
    """Unique identifier for the schedule."""

    inserted_at: datetime
    """Timestamp when the resource was created."""

    recipient: Recipient
    """A recipient of a notification, which is either a user or an object."""

    repeats: List[ScheduleRepeatRule]
    """The repeat rule for the schedule."""

    updated_at: datetime
    """The timestamp when the resource was last updated."""

    workflow: str
    """The workflow the schedule is applied to."""

    api_typename: Optional[str] = FieldInfo(alias="__typename", default=None)
    """The typename of the schema."""

    actor: Optional[Recipient] = None
    """A recipient of a notification, which is either a user or an object."""

    data: Optional[Dict[str, object]] = None
    """An optional map of data to pass into the workflow execution.

    There is a 1024 byte limit on the size of any single string value (with the
    exception of [email attachments](/integrations/email/attachments)), and a 10MB
    limit on the size of the full `data` payload.
    """

    last_occurrence_at: Optional[datetime] = None
    """The last occurrence of the schedule."""

    next_occurrence_at: Optional[datetime] = None
    """The next occurrence of the schedule."""

    tenant: Optional[str] = None
    """The tenant to trigger the workflow for.

    Triggering with a tenant will use any tenant-level overrides associated with the
    tenant object, and all messages produced from workflow runs will be tagged with
    the tenant.
    """
