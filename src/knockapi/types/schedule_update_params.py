# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .recipient_reference_param import RecipientReferenceParam
from .schedule_repeat_rule_param import ScheduleRepeatRuleParam
from .inline_tenant_request_param import InlineTenantRequestParam

__all__ = ["ScheduleUpdateParams"]


class ScheduleUpdateParams(TypedDict, total=False):
    schedule_ids: Required[List[str]]
    """A list of schedule IDs."""

    actor: Optional[RecipientReferenceParam]
    """
    A reference to a recipient, either a user identifier (string) or an object
    reference (ID, collection).
    """

    data: Optional[Dict[str, object]]
    """An optional map of data to pass into the workflow execution.

    There is a 1024 byte limit on the size of any single string value (with the
    exception of [email attachments](/integrations/email/attachments)), and a 10MB
    limit on the size of the full `data` payload.
    """

    ending_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The ending date and time for the schedule."""

    repeats: Iterable[ScheduleRepeatRuleParam]
    """The repeat rule for the schedule."""

    scheduled_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The starting date and time for the schedule."""

    tenant: Optional[InlineTenantRequestParam]
    """An request to set a tenant inline."""
