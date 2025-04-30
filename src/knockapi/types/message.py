# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .recipient_reference import RecipientReference

__all__ = ["Message", "Source"]


class Source(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    categories: List[str]
    """The categories associated with the message."""

    key: str
    """The key of the workflow that triggered the message."""

    version_id: str
    """The ID of the version of the workflow that triggered the message."""


class Message(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the message."""

    api_typename: Optional[str] = FieldInfo(alias="__typename", default=None)
    """The typename of the schema."""

    actors: Optional[List[RecipientReference]] = None
    """One or more actors that are associated with this message.

    Note: this is a list that can contain up to 10 actors if the message is produced
    from a [batch](/designing-workflows/batch-function).
    """

    archived_at: Optional[datetime] = None
    """Timestamp when the message was archived."""

    channel_id: Optional[str] = None
    """The ID for the channel the message was sent through."""

    clicked_at: Optional[datetime] = None
    """Timestamp when the message was clicked."""

    data: Optional[Dict[str, object]] = None
    """Data associated with the message’s workflow run.

    Includes the workflow trigger request’s `data` payload merged with any
    additional data returned by a
    [fetch function](/designing-workflows/fetch-function). For messages produced
    after a [batch step](/designing-workflows/batch-function), includes the payload
    `data` from the most-recent trigger request (the final `activity` in the batch).
    """

    engagement_statuses: Optional[List[Literal["seen", "read", "interacted", "link_clicked", "archived"]]] = None
    """A list of engagement statuses."""

    inserted_at: Optional[datetime] = None
    """Timestamp when the resource was created."""

    interacted_at: Optional[datetime] = None
    """Timestamp when the message was interacted with."""

    link_clicked_at: Optional[datetime] = None
    """Timestamp when a link in the message was clicked."""

    metadata: Optional[Dict[str, object]] = None
    """The metadata associated with the message."""

    read_at: Optional[datetime] = None
    """Timestamp when the message was read."""

    recipient: Optional[RecipientReference] = None
    """
    A reference to a recipient, either a user identifier (string) or an object
    reference (ID, collection).
    """

    scheduled_at: Optional[datetime] = None
    """Timestamp when the message was scheduled to be sent."""

    seen_at: Optional[datetime] = None
    """Timestamp when the message was seen."""

    source: Optional[Source] = None
    """The workflow that triggered the message."""

    status: Optional[
        Literal["queued", "sent", "delivered", "delivery_attempted", "undelivered", "not_sent", "bounced"]
    ] = None
    """The message delivery status."""

    tenant: Optional[str] = None
    """The ID of the `tenant` associated with the message.

    Only present when a `tenant` is provided on a workflow trigger request.
    """

    updated_at: Optional[datetime] = None
    """The timestamp when the resource was last updated."""

    workflow: Optional[str] = None
    """The key of the workflow that generated the message."""
