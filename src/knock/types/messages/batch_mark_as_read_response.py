# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "BatchMarkAsReadResponse",
    "BatchMarkAsReadResponseItem",
    "BatchMarkAsReadResponseItemActor",
    "BatchMarkAsReadResponseItemActorObjectReference",
    "BatchMarkAsReadResponseItemRecipient",
    "BatchMarkAsReadResponseItemRecipientObjectReference",
    "BatchMarkAsReadResponseItemSource",
]


class BatchMarkAsReadResponseItemActorObjectReference(BaseModel):
    id: str
    """An object identifier"""

    collection: str
    """The collection the object belongs to"""


BatchMarkAsReadResponseItemActor: TypeAlias = Union[str, BatchMarkAsReadResponseItemActorObjectReference]


class BatchMarkAsReadResponseItemRecipientObjectReference(BaseModel):
    id: str
    """An object identifier"""

    collection: str
    """The collection the object belongs to"""


BatchMarkAsReadResponseItemRecipient: TypeAlias = Union[str, BatchMarkAsReadResponseItemRecipientObjectReference]


class BatchMarkAsReadResponseItemSource(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    categories: List[str]
    """The workflow categories"""

    key: str
    """The workflow key"""

    version_id: str
    """The source version ID"""


class BatchMarkAsReadResponseItem(BaseModel):
    id: Optional[str] = None
    """The message ID"""

    api_typename: Optional[str] = FieldInfo(alias="__typename", default=None)

    actors: Optional[List[BatchMarkAsReadResponseItemActor]] = None
    """A list of actor representations associated with the message (up to 10)"""

    archived_at: Optional[datetime] = None
    """Timestamp when message was archived"""

    channel_id: Optional[str] = None
    """Channel ID associated with the message"""

    clicked_at: Optional[datetime] = None
    """Timestamp when message was clicked"""

    data: Optional[Dict[str, object]] = None
    """Additional message data"""

    engagement_statuses: Optional[List[Literal["seen", "read", "interacted", "link_clicked", "archived"]]] = None
    """List of engagement statuses"""

    inserted_at: Optional[datetime] = None
    """Timestamp of creation"""

    interacted_at: Optional[datetime] = None
    """Timestamp when message was interacted with"""

    link_clicked_at: Optional[datetime] = None
    """Timestamp when a link in the message was clicked"""

    metadata: Optional[Dict[str, object]] = None
    """Message metadata"""

    read_at: Optional[datetime] = None
    """Timestamp when message was read"""

    recipient: Optional[BatchMarkAsReadResponseItemRecipient] = None
    """
    A reference to a recipient, either a user identifier (string) or an object
    reference (id, collection).
    """

    scheduled_at: Optional[datetime] = None
    """Timestamp when message was scheduled for"""

    seen_at: Optional[datetime] = None
    """Timestamp when message was seen"""

    source: Optional[BatchMarkAsReadResponseItemSource] = None
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


BatchMarkAsReadResponse: TypeAlias = List[BatchMarkAsReadResponseItem]
