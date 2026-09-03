# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PreferenceCenterGenerateSignedURLResponse"]


class PreferenceCenterGenerateSignedURLResponse(BaseModel):
    """A signed preference center URL and token for a user."""

    token: str
    """
    The signed JWT token for the preference center, usable as the `/p/{token}` path
    segment.
    """

    url: str
    """The full URL to the preference center for the user."""
