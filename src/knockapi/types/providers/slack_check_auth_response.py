# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SlackCheckAuthResponse", "Connection"]


class Connection(BaseModel):
    ok: bool

    reason: Optional[str] = None


class SlackCheckAuthResponse(BaseModel):
    connection: Connection
