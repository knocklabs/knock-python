# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PreferenceCenterBrandingConfig"]


class PreferenceCenterBrandingConfig(BaseModel):
    """
    The branding for the preference center, sourced from public environment variables.
    """

    icon_url: Optional[str] = None
    """The icon URL for the preference center.

    Must point to a valid image with an image MIME type.
    """

    logo_url: Optional[str] = None
    """The logo URL for the preference center.

    Must point to a valid image with an image MIME type.
    """

    primary_color: Optional[str] = None
    """The primary color for the preference center, provided as a hex value."""

    primary_color_contrast: Optional[str] = None
    """The primary color contrast for the preference center, provided as a hex value."""
