# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Message", "Actor", "ActorUnionMember1", "Recipient", "RecipientUnionMember1", "Source"]


class ActorUnionMember1(BaseModel):
    id: str
    """An object identifier"""

    collection: str
    """The collection the object belongs to"""


Actor: TypeAlias = Union[str, ActorUnionMember1]


class RecipientUnionMember1(BaseModel):
    id: str
    """An object identifier"""

    collection: str
    """The collection the object belongs to"""


Recipient: TypeAlias = Union[str, RecipientUnionMember1]


class Source(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    categories: List[str]
    """The workflow categories"""

    key: str
    """The workflow key"""

    version_id: str
    """The source version ID"""


class Message(BaseModel):
    id: Optional[str] = None
    """The message ID"""

    api_typename: Optional[str] = FieldInfo(alias="__typename", default=None)

    actors: Optional[List[Actor]] = None
    """A list of actor representations associated with the message (up to 10)"""

    archived_at: Optional[datetime] = None
    """Timestamp when message was archived"""

    channel_id: Optional[str] = None
    """Channel ID associated with the message"""

    clicked_at: Optional[datetime] = None
    """Timestamp when message was clicked"""

    data: Optional[object] = None
    """Additional message data"""

    engagement_statuses: Optional[List[Literal["seen", "read", "interacted", "link_clicked", "archived"]]] = None
    """List of engagement statuses"""

    inserted_at: Optional[datetime] = None
    """Timestamp of creation"""

    interacted_at: Optional[datetime] = None
    """Timestamp when message was interacted with"""

    link_clicked_at: Optional[datetime] = None
    """Timestamp when a link in the message was clicked"""

    metadata: Optional[object] = None
    """Message metadata"""

    read_at: Optional[datetime] = None
    """Timestamp when message was read"""

    recipient: Optional[Recipient] = None
    """
    A reference to a recipient, either a user identifier (string) or an object
    reference (id, collection).
    """

    scheduled_at: Optional[datetime] = None
    """Timestamp when message was scheduled for"""

    seen_at: Optional[datetime] = None
    """Timestamp when message was seen"""

    source: Optional[Source] = None
    """Source information"""

    status: Optional[
        Literal["queued", "sent", "delivered", "delivery_attempted", "undelivered", "not_sent", "bounced"]
    ] = None
    """Message delivery status"""

    tenant: Optional[str] = None
    """Tenant ID that the message belongs to"""

    updated_at: Optional[datetime] = None
    """Timestamp of last update"""

    workflow: Optional[str] = None
    """Workflow key used to create the message"""
