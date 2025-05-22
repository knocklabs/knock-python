# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..recipient_request_param import RecipientRequestParam
from ..schedule_repeat_rule_param import ScheduleRepeatRuleParam
from ..inline_tenant_request_param import InlineTenantRequestParam

__all__ = ["BulkCreateParams", "Schedule"]


class BulkCreateParams(TypedDict, total=False):
    schedules: Required[Iterable[Schedule]]
    """A list of schedules."""


class Schedule(TypedDict, total=False):
    workflow: Required[str]
    """The key of the workflow."""

    actor: Optional[RecipientRequestParam]
    """Specifies a recipient in a request.

    This can either be a user identifier (string), an inline user request (object),
    or an inline object request, which is determined by the presence of a
    `collection` property.
    """

    data: Optional[Dict[str, object]]
    """An optional map of data to pass into the workflow execution.

    There is a 1024 byte limit on the size of any single string value (with the
    exception of [email attachments](/integrations/email/attachments)), and a 10MB
    limit on the size of the full `data` payload.
    """

    ending_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The ending date and time for the schedule."""

    recipient: RecipientRequestParam
    """Specifies a recipient in a request.

    This can either be a user identifier (string), an inline user request (object),
    or an inline object request, which is determined by the presence of a
    `collection` property.
    """

    repeats: Iterable[ScheduleRepeatRuleParam]
    """The repeat rule for the schedule."""

    scheduled_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The starting date and time for the schedule."""

    tenant: Optional[InlineTenantRequestParam]
    """An request to set a tenant inline."""
