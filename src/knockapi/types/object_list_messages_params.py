# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ObjectListMessagesParams"]


class ObjectListMessagesParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    channel_id: str
    """The unique identifier for the channel."""

    engagement_status: List[Literal["seen", "read", "interacted", "link_clicked", "archived"]]
    """The engagement status to filter messages by."""

    message_ids: List[str]
    """The message IDs to filter messages by."""

    page_size: int
    """The number of items per page."""

    source: str
    """The source of the message (workflow key)."""

    status: List[Literal["queued", "sent", "delivered", "delivery_attempted", "undelivered", "not_sent", "bounced"]]
    """The delivery status to filter messages by."""

    tenant: str
    """The unique identifier for the tenant."""

    trigger_data: str
    """The trigger data to filter messages by. Must be a valid JSON object."""

    workflow_categories: List[str]
    """The workflow categories to filter messages by."""

    workflow_recipient_run_id: str
    """The workflow recipient run ID to filter messages by."""

    workflow_run_id: str
    """The workflow run ID to filter messages by."""
