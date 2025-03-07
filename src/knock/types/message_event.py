# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageEvent", "Recipient", "RecipientObjectReference"]


class RecipientObjectReference(BaseModel):
    id: str
    """An object identifier"""

    collection: str
    """The collection the object belongs to"""


Recipient: TypeAlias = Union[str, RecipientObjectReference]


class MessageEvent(BaseModel):
    id: str

    api_typename: str = FieldInfo(alias="__typename")

    inserted_at: datetime

    recipient: Recipient
    """
    A reference to a recipient, either a user identifier (string) or an object
    reference (id, collection).
    """

    type: Literal[
        "message.queued",
        "message.sent",
        "message.delivered",
        "message.undelivered",
        "message.bounced",
        "message.read",
        "message.unread",
        "message.link_clicked",
        "message.interacted",
        "message.seen",
        "message.unseen",
        "message.archived",
        "message.unarchived",
    ]

    data: Optional[Dict[str, object]] = None
    """The data associated with the event. Only present for some event types"""
