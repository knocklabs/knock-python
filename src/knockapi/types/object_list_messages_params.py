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
    """Limits the results to items with the corresponding channel id."""

    engagement_status: List[Literal["seen", "read", "interacted", "link_clicked", "archived"]]
    """One or more engagement statuses.

    Limits results to messages with the given engagement status(es).
    """

    message_ids: List[str]
    """Limits the results to only the message ids given (max 50).

    Note: when using this option, the results will be subject to any other filters
    applied to the query.
    """

    page_size: int
    """The number of items per page."""

    source: str
    """Limits the results to only items of the source workflow."""

    status: List[Literal["queued", "sent", "delivered", "delivery_attempted", "undelivered", "not_sent", "bounced"]]
    """One or more delivery statuses.

    Limits results to messages with the given delivery status(es).
    """

    tenant: str
    """
    Limits the results to items with the corresponding tenant, or where the tenant
    is empty.
    """

    trigger_data: str
    """Limits the results to only items that were generated with the given data."""

    workflow_categories: List[str]
    """Limits the results to only items related to any of the provided categories."""

    workflow_recipient_run_id: str
    """Limits the results to messages for a specific recipient's workflow run."""

    workflow_run_id: str
    """Limits the results to messages triggered by the top-level workflow run ID."""
