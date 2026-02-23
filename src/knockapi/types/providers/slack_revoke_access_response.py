# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SlackRevokeAccessResponse"]


class SlackRevokeAccessResponse(BaseModel):
    """A response indicating the operation was successful."""

    ok: Optional[str] = None
    """OK response."""
