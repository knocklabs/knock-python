# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .preference_center_branding_config import PreferenceCenterBrandingConfig

__all__ = ["PreferenceCenterGetConfigResponse", "Branding", "Config", "ConfigRow"]


class Branding(PreferenceCenterBrandingConfig):
    """
    The branding for the preference center, sourced from public environment variables.
    """

    dark: Optional[PreferenceCenterBrandingConfig] = None
    """
    The branding for the preference center, sourced from public environment
    variables.
    """


class ConfigRow(BaseModel):
    """A preference row in the preference center configuration."""

    name: str
    """The display name of the preference row."""

    type: Literal["workflow", "channel", "category", "channel_types", "commercial_subscribed"]
    """The type of this preference row.

    `workflow` targets a workflow, `channel` targets a specific channel, `category`
    targets a workflow category, `channel_types` controls per-channel-type
    opt-in/out, and `commercial_subscribed` is the commercial notification toggle.
    """

    channel_types: Optional[
        List[
            Literal[
                "email", "in_app", "in_app_feed", "in_app_guide", "sms", "push", "chat", "http", "log", "deferred_log"
            ]
        ]
    ] = None
    """The list of channel types this preference is scoped to.

    An empty list (or `null`) means the preference applies to all channel types.
    Present for `workflow`, `category`, and `channel_types` types.
    """

    description: Optional[str] = None
    """A description shown below the preference row name."""

    identifier: Optional[str] = None
    """The category name, workflow key, or channel ID this row controls (e.g.

    `marketing`, `new-project-mentions`, or a channel UUID). Present for `workflow`,
    `channel`, and `category` types.
    """


class Config(BaseModel):
    """The preference center configuration data containing the rows to display."""

    body: str
    """The body text displayed below the title."""

    rows: List[ConfigRow]
    """An ordered list of rows to display in the preference center."""

    title: str
    """The title displayed at the top of the preference center."""

    show_account_name: Optional[bool] = None
    """Whether the account name should be displayed in the preference center."""


class PreferenceCenterGetConfigResponse(BaseModel):
    """The preference center configuration for an environment.

    Controls whether the preference center is enabled and defines the rows displayed in the UI.
    """

    account_name: Optional[str] = None
    """The name of the account that the preference center is associated with."""

    branding: Branding
    """
    The branding for the preference center, sourced from public environment
    variables.
    """

    config: Config
    """The preference center configuration data containing the rows to display."""

    enabled: bool
    """Whether the preference center is enabled for this environment."""

    user_email: Optional[str] = None
    """
    A display label for the user that the preference center is associated with,
    resolved as email, then user id.
    """

    knock_branding_required: Optional[bool] = None
    """Whether Knock branding is required in the preference center."""
