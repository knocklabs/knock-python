# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BulkUpdateMessageStatusParams"]


class BulkUpdateMessageStatusParams(TypedDict, total=False):
    channel_id: Required[str]

    archived: Literal["exclude", "include", "only"]

    delivery_status: Literal["queued", "sent", "delivered", "delivery_attempted", "undelivered", "not_sent", "bounced"]

    engagement_status: Literal[
        "seen", "unseen", "read", "unread", "archived", "unarchived", "link_clicked", "interacted"
    ]

    has_tenant: bool

    newer_than: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    older_than: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    recipient_ids: List[str]

    tenants: List[str]

    trigger_data: str

    workflows: List[str]
