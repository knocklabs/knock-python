# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .recipient_reference import RecipientReference

__all__ = ["MessageEvent"]


class MessageEvent(BaseModel):
    id: str
    """The unique identifier for the message event."""

    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    inserted_at: datetime
    """Timestamp when the event was created."""

    recipient: RecipientReference
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
