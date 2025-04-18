# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CensusCustomDestinationResponse"]


class CensusCustomDestinationResponse(BaseModel):
    id: Optional[str] = None
    """The request ID."""

    result: Optional[object] = None
    """The result of the RPC call."""
