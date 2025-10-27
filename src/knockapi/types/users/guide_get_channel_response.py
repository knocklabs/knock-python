# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "GuideGetChannelResponse",
    "Entry",
    "EntryActivationURLPattern",
    "EntryActivationURLRule",
    "EntryStep",
    "EntryStepMessage",
    "GuideGroup",
]


class EntryActivationURLPattern(BaseModel):
    directive: Optional[str] = None
    """The directive for the URL pattern ('allow' or 'block')"""

    pathname: Optional[str] = None
    """The pathname pattern to match (supports wildcards like /\\**)"""


class EntryActivationURLRule(BaseModel):
    argument: Optional[str] = None
    """The value to compare against"""

    directive: Optional[str] = None
    """The directive for the URL pattern ('allow' or 'block')"""

    operator: Optional[str] = None
    """The comparison operator ('contains' or 'equal_to')"""

    variable: Optional[str] = None
    """The variable to evaluate ('pathname')"""


class EntryStepMessage(BaseModel):
    id: Optional[str] = None

    archived_at: Optional[datetime] = None

    interacted_at: Optional[datetime] = None

    link_clicked_at: Optional[datetime] = None

    read_at: Optional[datetime] = None

    seen_at: Optional[datetime] = None


class EntryStep(BaseModel):
    content: Optional[Dict[str, object]] = None

    message: Optional[EntryStepMessage] = None

    ref: Optional[str] = None

    schema_key: Optional[str] = None

    schema_semver: Optional[str] = None

    schema_variant_key: Optional[str] = None


class Entry(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the guide."""

    api_typename: Optional[str] = FieldInfo(alias="__typename", default=None)
    """The typename of the schema."""

    activation_url_patterns: Optional[List[EntryActivationURLPattern]] = None
    """
    A list of URL Patterns to evaluate user's current location to activate the
    guide, if matched
    """

    activation_url_rules: Optional[List[EntryActivationURLRule]] = None
    """
    A list of URL rules to evaluate user's current location to activate the guide,
    if matched
    """

    active: Optional[bool] = None
    """Whether the guide is active."""

    bypass_global_group_limit: Optional[bool] = None

    channel_id: Optional[str] = None

    inserted_at: Optional[datetime] = None

    key: Optional[str] = None
    """The key of the guide."""

    semver: Optional[str] = None

    steps: Optional[List[EntryStep]] = None

    type: Optional[str] = None
    """The type of the guide."""

    updated_at: Optional[datetime] = None


class GuideGroup(BaseModel):
    api_typename: Optional[str] = FieldInfo(alias="__typename", default=None)

    display_interval: Optional[int] = None

    display_sequence: Optional[List[str]] = None

    inserted_at: Optional[datetime] = None

    key: Optional[str] = None

    updated_at: Optional[datetime] = None


class GuideGetChannelResponse(BaseModel):
    entries: List[Entry]
    """A list of guides."""

    guide_group_display_logs: Dict[str, datetime]
    """A map of guide group keys to their last display timestamps."""

    guide_groups: List[GuideGroup]
    """A list of guide groups with their display sequences and intervals."""
