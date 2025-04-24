# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["GuideMarkMessageAsSeenResponse"]


class GuideMarkMessageAsSeenResponse(BaseModel):
    status: str
    """The status of a guide's action."""
