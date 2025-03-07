# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.schedule_repeat_rule import ScheduleRepeatRule
from .shared_params.inline_tenant_request import InlineTenantRequest

__all__ = ["ScheduleCreateParams", "Recipient", "RecipientObjectReference"]


class ScheduleCreateParams(TypedDict, total=False):
    recipients: Required[List[Recipient]]

    repeats: Required[Iterable[ScheduleRepeatRule]]

    workflow: Required[str]

    data: Optional[Dict[str, object]]

    ending_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    scheduled_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    tenant: Optional[InlineTenantRequest]
    """An inline tenant request"""


class RecipientObjectReference(TypedDict, total=False):
    id: Required[str]
    """An object identifier"""

    collection: Required[str]
    """The collection the object belongs to"""


Recipient: TypeAlias = Union[str, RecipientObjectReference]
