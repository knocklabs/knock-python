# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .recipients.preference_set import PreferenceSet

__all__ = ["Tenant", "Settings", "SettingsBranding"]


class SettingsBranding(BaseModel):
    icon_url: Optional[str] = None
    """The icon URL for the tenant.

    Must point to a valid image with an image MIME type.
    """

    logo_url: Optional[str] = None
    """The logo URL for the tenant.

    Must point to a valid image with an image MIME type.
    """

    primary_color: Optional[str] = None
    """The primary color for the tenant, provided as a hex value."""

    primary_color_contrast: Optional[str] = None
    """The primary color contrast for the tenant, provided as a hex value."""


class Settings(BaseModel):
    branding: Optional[SettingsBranding] = None
    """The branding for the tenant."""

    preference_set: Optional[PreferenceSet] = None
    """
    A preference set represents a specific set of notification preferences for a
    recipient. A recipient can have multiple preference sets.
    """


class Tenant(BaseModel):
    id: str
    """The unique identifier for the tenant."""

    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    name: Optional[str] = None
    """An optional name for the tenant."""

    settings: Optional[Settings] = None
    """The settings for the tenant. Includes branding and preference set."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
