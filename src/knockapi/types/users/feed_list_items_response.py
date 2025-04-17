# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..activity import Activity
from ..recipient import Recipient

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
    """The content of the block in a message in an app feed."""

    name: str
    """The name of the block in a message in an app feed."""

    rendered: str
    """The rendered HTML version of the content."""

    type: Literal["markdown", "text"]
    """The type of block in a message in an app feed."""


class BlockMessageInAppFeedButtonSetBlockButton(BaseModel):
    action: str
    """The action to take when the button is clicked."""

    label: str
    """The label of the button."""

    name: str
    """The name of the button."""


class BlockMessageInAppFeedButtonSetBlock(BaseModel):
    buttons: List[BlockMessageInAppFeedButtonSetBlockButton]
    """A list of buttons in an in app feed message."""

    name: str
    """The name of the button set in a message in an app feed."""

    type: Literal["button_set"]
    """The type of block in a message in an app feed."""


Block: TypeAlias = Union[BlockMessageInAppFeedContentBlock, BlockMessageInAppFeedButtonSetBlock]


class Source(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    categories: List[str]
    """Categories this workflow belongs to."""

    key: str
    """The key of the workflow."""

    version_id: str
    """The workflow version ID."""


class FeedListItemsResponse(BaseModel):
    id: str
    """Unique identifier for the feed."""

    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    activities: List[Activity]
    """List of activities associated with this feed item."""

    actors: List[Recipient]
    """List of actors associated with this feed item."""

    blocks: List[Block]
    """Content blocks that make up the feed item."""

    data: Optional[Dict[str, object]] = None
    """Additional data associated with the feed item."""

    inserted_at: str
    """Timestamp when the resource was created."""

    source: Source
    """Source information for the feed item."""

    tenant: Optional[str] = None
    """Tenant ID that the feed item belongs to."""

    total_activities: int
    """Total number of activities related to this feed item."""

    total_actors: int
    """Total number of actors related to this feed item."""

    updated_at: str
    """The timestamp when the resource was last updated."""

    archived_at: Optional[str] = None
    """Timestamp when the feed item was archived."""

    clicked_at: Optional[str] = None
    """Timestamp when the feed item was clicked."""

    interacted_at: Optional[str] = None
    """Timestamp when the feed item was interacted with."""

    link_clicked_at: Optional[str] = None
    """Timestamp when a link within the feed item was clicked."""

    read_at: Optional[str] = None
    """Timestamp when the feed item was marked as read."""

    seen_at: Optional[str] = None
    """Timestamp when the feed item was marked as seen."""
