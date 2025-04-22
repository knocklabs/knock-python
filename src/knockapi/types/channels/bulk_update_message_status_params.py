# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BulkUpdateMessageStatusParams"]


class BulkUpdateMessageStatusParams(TypedDict, total=False):
    archived: Literal["exclude", "include", "only"]
    """Limits the results to messages with the given archived status."""

    delivery_status: Literal["queued", "sent", "delivered", "delivery_attempted", "undelivered", "not_sent", "bounced"]
    """Limits the results to messages with the given delivery status."""

    engagement_status: Literal[
        "seen", "unseen", "read", "unread", "archived", "unarchived", "link_clicked", "interacted"
    ]
    """Limits the results to messages with the given engagement status."""

    has_tenant: bool
    """Limits the results to messages that have a tenant or not."""

    newer_than: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Limits the results to messages inserted after the given date."""

    older_than: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Limits the results to messages inserted before the given date."""

    recipient_ids: List[str]
    """Limits the results to messages with the given recipient IDs."""

    tenants: List[str]
    """Limits the results to messages with the given tenant IDs."""

    trigger_data: str
    """Limits the results to only messages that were generated with the given data.

    See [trigger data filtering](/api-reference/overview/trigger-data-filtering) for
    more information.
    """

    workflows: List[str]
    """Limits the results to messages with the given workflow keys."""
