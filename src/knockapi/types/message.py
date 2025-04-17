# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Message", "Actor", "ActorObjectReference", "Recipient", "RecipientObjectReference", "Source"]


class ActorObjectReference(BaseModel):
    id: Optional[str] = None
    """An identifier for the recipient object."""

    collection: Optional[str] = None
    """The collection the recipient object belongs to."""


Actor: TypeAlias = Union[str, ActorObjectReference]


class RecipientObjectReference(BaseModel):
    id: Optional[str] = None
    """An identifier for the recipient object."""

    collection: Optional[str] = None
    """The collection the recipient object belongs to."""


Recipient: TypeAlias = Union[str, RecipientObjectReference]


class Source(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    categories: List[str]
    """The categories associated with the message."""

    key: str
    """The key of the source that triggered the message."""

    version_id: str
    """The id of the version of the source that triggered the message."""


class Message(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the message."""

    api_typename: Optional[str] = FieldInfo(alias="__typename", default=None)
    """The typename of the schema."""

    actors: Optional[List[Actor]] = None
    """One or more actors that are associated with this message.

    Note: this is a list that can contain up to 10 actors if the message is produced
    from a batch.
    """

    archived_at: Optional[datetime] = None
    """Timestamp when the message was archived."""

    channel_id: Optional[str] = None
    """The id for the channel the message was sent through."""

    clicked_at: Optional[datetime] = None
    """Timestamp when the message was clicked."""

    data: Optional[Dict[str, object]] = None
    """Data from the activities linked to the message"""

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

    recipient: Optional[Recipient] = None
    """
    A reference to a recipient, either a user identifier (string) or an object
    reference (id, collection).
    """

    scheduled_at: Optional[datetime] = None
    """Timestamp when the message was scheduled to be sent."""

    seen_at: Optional[datetime] = None
    """Timestamp when the message was seen."""

    source: Optional[Source] = None
    """The source that triggered the message."""

    status: Optional[
        Literal["queued", "sent", "delivered", "delivery_attempted", "undelivered", "not_sent", "bounced"]
    ] = None
    """The message delivery status."""

    tenant: Optional[str] = None
    """The id for the tenant set for the message."""

    updated_at: Optional[datetime] = None
    """The timestamp when the resource was last updated."""

    workflow: Optional[str] = None
    """The key of the worklfow that generated the message."""
