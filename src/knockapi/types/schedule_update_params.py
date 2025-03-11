# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .recipient_request_param import RecipientRequestParam
from .schedule_repeat_rule_param import ScheduleRepeatRuleParam
from .inline_tenant_request_param import InlineTenantRequestParam

__all__ = ["ScheduleUpdateParams"]


class ScheduleUpdateParams(TypedDict, total=False):
    schedule_ids: Required[List[str]]

    actor: Optional[RecipientRequestParam]
    """Specifies a recipient in a request.

    This can either be a user identifier (string), an inline user request (object),
    or an inline object request, which is determined by the presence of a
    `collection` property.
    """

    data: Optional[Dict[str, object]]

    ending_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    repeats: Iterable[ScheduleRepeatRuleParam]

    scheduled_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    tenant: Optional[InlineTenantRequestParam]
    """An inline tenant request"""
