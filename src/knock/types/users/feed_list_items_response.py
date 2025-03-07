# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..activity import Activity
from ..shared.recipient import Recipient

__all__ = [
    "FeedListItemsResponse",
    "Block",
    "BlockMessageInAppFeedContentBlock",
    "BlockMessageInAppFeedButtonSetBlock",
    "BlockMessageInAppFeedButtonSetBlockButton",
    "Source",
]


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
