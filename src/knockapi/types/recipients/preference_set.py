# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..shared.condition import Condition
from .preference_set_channel_types import PreferenceSetChannelTypes

__all__ = [
    "PreferenceSet",
    "Categories",
    "CategoriesPreferenceSetWorkflowCategorySettingObject",
    "CategoriesPreferenceSetWorkflowCategorySettingObjectChannels",
    "CategoriesPreferenceSetWorkflowCategorySettingObjectChannelsPreferenceSetChannelSetting",
    "Channels",
    "ChannelsPreferenceSetChannelSetting",
    "Workflows",
    "WorkflowsPreferenceSetWorkflowCategorySettingObject",
    "WorkflowsPreferenceSetWorkflowCategorySettingObjectChannels",
    "WorkflowsPreferenceSetWorkflowCategorySettingObjectChannelsPreferenceSetChannelSetting",
]


class CategoriesPreferenceSetWorkflowCategorySettingObjectChannelsPreferenceSetChannelSetting(BaseModel):
    conditions: List[Condition]
    """A list of conditions to apply to a specific channel."""


CategoriesPreferenceSetWorkflowCategorySettingObjectChannels: TypeAlias = Union[
    bool, CategoriesPreferenceSetWorkflowCategorySettingObjectChannelsPreferenceSetChannelSetting
]


class CategoriesPreferenceSetWorkflowCategorySettingObject(BaseModel):
    channel_types: Optional[PreferenceSetChannelTypes] = None
    """Channel type preferences."""

    channels: Optional[Dict[str, CategoriesPreferenceSetWorkflowCategorySettingObjectChannels]] = None
    """Channel preferences."""

    conditions: Optional[List[Condition]] = None
    """A list of conditions to apply to a channel type."""


Categories: TypeAlias = Union[bool, CategoriesPreferenceSetWorkflowCategorySettingObject]


class ChannelsPreferenceSetChannelSetting(BaseModel):
    conditions: List[Condition]
    """A list of conditions to apply to a specific channel."""


Channels: TypeAlias = Union[bool, ChannelsPreferenceSetChannelSetting]


class WorkflowsPreferenceSetWorkflowCategorySettingObjectChannelsPreferenceSetChannelSetting(BaseModel):
    conditions: List[Condition]
    """A list of conditions to apply to a specific channel."""


WorkflowsPreferenceSetWorkflowCategorySettingObjectChannels: TypeAlias = Union[
    bool, WorkflowsPreferenceSetWorkflowCategorySettingObjectChannelsPreferenceSetChannelSetting
]


class WorkflowsPreferenceSetWorkflowCategorySettingObject(BaseModel):
    channel_types: Optional[PreferenceSetChannelTypes] = None
    """Channel type preferences."""

    channels: Optional[Dict[str, WorkflowsPreferenceSetWorkflowCategorySettingObjectChannels]] = None
    """Channel preferences."""

    conditions: Optional[List[Condition]] = None
    """A list of conditions to apply to a channel type."""


Workflows: TypeAlias = Union[bool, WorkflowsPreferenceSetWorkflowCategorySettingObject]


class PreferenceSet(BaseModel):
    id: str
    """Unique identifier for the preference set."""

    categories: Optional[Dict[str, Categories]] = None
    """
    An object where the key is the category and the values are the preference
    settings for that category.
    """

    channel_types: Optional[PreferenceSetChannelTypes] = None
    """Channel type preferences."""

    channels: Optional[Dict[str, Channels]] = None
    """Channel preferences."""

    commercial_subscribed: Optional[bool] = None
    """Whether the recipient is subscribed to commercial communications.

    When false, the recipient will not receive commercial workflow notifications.
    """

    workflows: Optional[Dict[str, Workflows]] = None
    """
    An object where the key is the workflow key and the values are the preference
    settings for that workflow.
    """
