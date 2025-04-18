# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BulkUpdateMessageStatusParams"]


class BulkUpdateMessageStatusParams(TypedDict, total=False):
    archived: Literal["exclude", "include", "only"]
    """The archived status to filter messages by."""

    delivery_status: Literal["queued", "sent", "delivered", "delivery_attempted", "undelivered", "not_sent", "bounced"]
    """The delivery status to filter messages by."""

    engagement_status: Literal[
        "seen", "unseen", "read", "unread", "archived", "unarchived", "link_clicked", "interacted"
    ]
    """The engagement status to filter messages by."""

    has_tenant: bool
    """Whether to include only messages that have a tenant or not."""

    newer_than: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The timestamp to filter messages by.

    Only include messages created after this timestamp.
    """

    older_than: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The timestamp to filter messages by.

    Only include messages created before this timestamp.
    """

    recipient_gids: List[str]
    """The recipient GIDs to filter messages by."""

    recipient_ids: List[str]
    """The recipient IDs to filter messages by."""

    tenants: List[str]
    """The tenant IDs to filter messages by."""

    trigger_data: str
    """The trigger data to filter messages by. Must be a valid JSON object."""

    workflows: List[str]
    """The workflow keys to filter messages by."""
