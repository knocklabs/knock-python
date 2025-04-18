# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["GuideGetChannelResponse", "Guide", "Recipient"]


class Guide(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the guide."""

    content: Optional[str] = None
    """The content of the guide."""

    metadata: Optional[Dict[str, object]] = None
    """The metadata of the guide."""

    title: Optional[str] = None
    """The title of the guide."""


class Recipient(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the recipient."""


class GuideGetChannelResponse(BaseModel):
    guides: List[Guide]
    """A list of guides."""

    recipient: Optional[Recipient] = None
    """The recipient of the guide."""
