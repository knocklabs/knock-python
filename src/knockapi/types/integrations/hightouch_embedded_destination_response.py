# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["HightouchEmbeddedDestinationResponse"]


class HightouchEmbeddedDestinationResponse(BaseModel):
    id: Optional[str] = None
    """The request ID."""

    result: Optional[Dict[str, object]] = None
    """The result of the RPC call."""
