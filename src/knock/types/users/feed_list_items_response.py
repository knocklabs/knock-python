# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.recipient import Recipient

__all__ = [
    "FeedListItemsResponse",
    "Activity",
    "Block",
    "BlockMessageInAppFeedContentBlock",
    "BlockMessageInAppFeedButtonSetBlock",
    "BlockMessageInAppFeedButtonSetBlockButton",
    "Source",
]


class Activity(BaseModel):
    id: Optional[str] = None

    api_typename: Optional[str] = FieldInfo(alias="__typename", default=None)

    actor: Optional[Recipient] = None
    """A recipient, which is either a user or an object"""

    data: Optional[Dict[str, object]] = None
    """The data associated with the activity"""

    inserted_at: Optional[datetime] = None

    recipient: Optional[Recipient] = None
    """A recipient, which is either a user or an object"""

    updated_at: Optional[datetime] = None


class BlockMessageInAppFeedContentBlock(BaseModel):
    content: str

    name: str

    rendered: str

    type: Literal["markdown", "text"]


class BlockMessageInAppFeedButtonSetBlockButton(BaseModel):
    action: str

    label: str

    name: str


class BlockMessageInAppFeedButtonSetBlock(BaseModel):
    buttons: List[BlockMessageInAppFeedButtonSetBlockButton]

    name: str

    type: Literal["button_set"]


Block: TypeAlias = Union[BlockMessageInAppFeedContentBlock, BlockMessageInAppFeedButtonSetBlock]


class Source(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    categories: List[str]

    key: str

    version_id: str


class FeedListItemsResponse(BaseModel):
    id: str

    api_typename: str = FieldInfo(alias="__typename")

    activities: List[Activity]

    actors: List[Recipient]

    blocks: List[Block]

    data: Optional[Dict[str, object]] = None

    inserted_at: str

    source: Source

    tenant: Optional[str] = None

    total_activities: int

    total_actors: int

    updated_at: str

    archived_at: Optional[str] = None

    clicked_at: Optional[str] = None

    interacted_at: Optional[str] = None

    link_clicked_at: Optional[str] = None

    read_at: Optional[str] = None

    seen_at: Optional[str] = None
