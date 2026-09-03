# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MessageInAppFeedContentBlock"]


class MessageInAppFeedContentBlock(BaseModel):
    """A block in a message in an app feed."""

    content: str
    """The content of the block in a message in an app feed."""

    name: str
    """The name of the block in a message in an app feed."""

    rendered: str
    """The rendered HTML version of the content."""

    type: Literal["markdown", "text"]
    """The type of block in a message in an app feed."""
