# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ObjectListMessagesParams", "InsertedAt"]


class ObjectListMessagesParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    channel_id: str
    """Limits the results to items with the corresponding channel ID."""

    engagement_status: List[
        Literal["seen", "unseen", "read", "unread", "archived", "unarchived", "link_clicked", "interacted"]
    ]
    """Limits the results to messages with the given engagement status."""

    inserted_at: InsertedAt

    message_ids: List[str]
    """Limits the results to only the message IDs given (max 50).

    Note: when using this option, the results will be subject to any other filters
    applied to the query.
    """

    page_size: int
    """The number of items per page."""

    source: str
    """Limits the results to messages triggered by the given workflow key."""

    status: List[Literal["queued", "sent", "delivered", "delivery_attempted", "undelivered", "not_sent", "bounced"]]
    """Limits the results to messages with the given delivery status."""

    tenant: str
    """Limits the results to items with the corresponding tenant."""

    trigger_data: str
    """Limits the results to only messages that were generated with the given data.

    See [trigger data filtering](/api-reference/overview/trigger-data-filtering) for
    more information.
    """

    workflow_categories: List[str]
    """Limits the results to messages related to any of the provided categories."""

    workflow_recipient_run_id: str
    """Limits the results to messages for a specific recipient's workflow run."""

    workflow_run_id: str
    """
    Limits the results to messages associated with the top-level workflow run ID
    returned by the workflow trigger request.
    """


class InsertedAt(TypedDict, total=False):
    gt: str
    """Limits the results to messages inserted after the given date."""

    gte: str
    """Limits the results to messages inserted after or on the given date."""

    lt: str
    """Limits the results to messages inserted before the given date."""

    lte: str
    """Limits the results to messages inserted before or on the given date."""
