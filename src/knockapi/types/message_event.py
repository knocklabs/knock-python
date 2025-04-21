# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageEvent", "Recipient", "RecipientObjectReference"]


class RecipientObjectReference(BaseModel):
    id: Optional[str] = None
    """An identifier for the recipient object."""

    collection: Optional[str] = None
    """The collection the recipient object belongs to."""


Recipient: TypeAlias = Union[str, RecipientObjectReference]


class MessageEvent(BaseModel):
    id: str
    """The unique identifier for the message event."""

    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    inserted_at: datetime
    """Timestamp when the event was created."""

    recipient: Recipient
    """
    A reference to a recipient, either a user identifier (string) or an object
    reference (ID, collection).
    """

    type: Literal[
        "message.archived",
        "message.bounced",
        "message.delivered",
        "message.delivery_attempted",
        "message.interacted",
        "message.link_clicked",
        "message.not_sent",
        "message.queued",
        "message.read",
        "message.seen",
        "message.sent",
        "message.unarchived",
        "message.undelivered",
        "message.unread",
        "message.unseen",
    ]
    """The type of event that occurred."""

    data: Optional[Dict[str, object]] = None
    """The data associated with the message event. Only present for some event types."""
