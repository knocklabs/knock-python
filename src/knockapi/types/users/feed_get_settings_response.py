# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["FeedGetSettingsResponse", "Features"]


class Features(BaseModel):
    """Features configuration for the user's feed."""

    branding_required: bool
    """Whether branding is required for the user's feed."""


class FeedGetSettingsResponse(BaseModel):
    """The response for the user's feed settings."""

    features: Features
    """Features configuration for the user's feed."""
