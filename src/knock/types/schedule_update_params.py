# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.recipient_request import RecipientRequest
from .shared_params.schedule_repeat_rule import ScheduleRepeatRule
from .shared_params.inline_tenant_request import InlineTenantRequest

__all__ = ["ScheduleUpdateParams"]


class ScheduleUpdateParams(TypedDict, total=False):
    schedule_ids: Required[List[str]]

    actor: Optional[RecipientRequest]
    """Specifies a recipient in a request.

    This can either be a user identifier (string), an inline user request (object),
    or an inline object request, which is determined by the presence of a
    `collection` property.
    """

    data: Optional[Dict[str, object]]

    ending_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    repeats: Iterable[ScheduleRepeatRule]

    scheduled_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    tenant: Optional[InlineTenantRequest]
    """An inline tenant request"""
