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
    """The key of the workflow or guide that triggered the message."""

    version_id: str
    """The ID of the version of the workflow or guide that triggered the message."""

    step_ref: Optional[str] = None
    """The step reference for the step in the workflow that generated the message."""

    type: Optional[Literal["broadcast", "workflow", "guide"]] = None
    """Whether this message was generated from a workflow, broadcast, or guide."""


class Message(BaseModel):
    id: str
    """The unique identifier for the message."""

    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    channel_id: str
    """The ID for the channel the message was sent through."""

    engagement_statuses: List[Literal["seen", "read", "interacted", "link_clicked", "archived"]]
    """A list of engagement statuses."""

    inserted_at: datetime
    """Timestamp when the resource was created."""

    recipient: RecipientReference
    """
    A reference to a recipient, either a user identifier (string) or an object
    reference (ID, collection).
    """

    source: Source
    """The workflow or guide that triggered the message."""

    status: Literal["queued", "sent", "delivered", "delivery_attempted", "undelivered", "not_sent", "bounced"]
    """The message delivery status."""

    updated_at: datetime
    """The timestamp when the resource was last updated."""

    actors: Optional[List[RecipientReference]] = None
    """One or more actors that are associated with this message.

    Note: this is a list that can contain up to 10 actors if the message is produced
    from a [batch](/designing-workflows/batch-function).
    """

    archived_at: Optional[datetime] = None
    """Timestamp when the message was archived."""

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

    interacted_at: Optional[datetime] = None
    """Timestamp when the message was interacted with."""

    link_clicked_at: Optional[datetime] = None
    """Timestamp when a link in the message was clicked."""

    metadata: Optional[Dict[str, object]] = None
    """The metadata associated with the message."""

    read_at: Optional[datetime] = None
    """Timestamp when the message was read."""

    scheduled_at: Optional[datetime] = None
    """Timestamp when the message was scheduled to be sent."""

    seen_at: Optional[datetime] = None
    """Timestamp when the message was seen."""

    tenant: Optional[str] = None
    """The ID of the `tenant` associated with the message.

    Only present when a `tenant` is provided on a workflow trigger request.
    """

    workflow: Optional[str] = None
    """The key of the workflow that generated the message."""
