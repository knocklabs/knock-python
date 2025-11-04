# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.condition import Condition
from .recipients.preference_set_channel_types_param import PreferenceSetChannelTypesParam
from .recipients.preference_set_channel_setting_param import PreferenceSetChannelSettingParam

__all__ = [
    "ObjectSetPreferencesParams",
    "Categories",
    "CategoriesPreferenceSetWorkflowCategorySettingObject",
    "CategoriesPreferenceSetWorkflowCategorySettingObjectChannels",
    "Channels",
    "Workflows",
    "WorkflowsPreferenceSetWorkflowCategorySettingObject",
    "WorkflowsPreferenceSetWorkflowCategorySettingObjectChannels",
]


class ObjectSetPreferencesParams(TypedDict, total=False):
    _persistence_strategy: Annotated[Literal["merge", "replace"], PropertyInfo(alias="__persistence_strategy__")]
    """Controls how the preference set is persisted.

    'replace' will completely replace the preference set, 'merge' will merge with
    existing preferences.
    """

    categories: Optional[Dict[str, Categories]]
    """
    An object where the key is the category and the values are the preference
    settings for that category.
    """

    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences."""

    channels: Optional[Dict[str, Channels]]
    """Channel preferences."""

    commercial_subscribed: Optional[bool]
    """Whether the recipient is subscribed to commercial communications.

    When false, the recipient will not receive commercial workflow notifications.
    """

    workflows: Optional[Dict[str, Workflows]]
    """
    An object where the key is the workflow key and the values are the preference
    settings for that workflow.
    """


CategoriesPreferenceSetWorkflowCategorySettingObjectChannels: TypeAlias = Union[bool, PreferenceSetChannelSettingParam]


class CategoriesPreferenceSetWorkflowCategorySettingObject(TypedDict, total=False):
    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences."""

    channels: Optional[Dict[str, CategoriesPreferenceSetWorkflowCategorySettingObjectChannels]]
    """Channel preferences."""

    conditions: Optional[Iterable[Condition]]
    """A list of conditions to apply to a channel type."""


Categories: TypeAlias = Union[bool, CategoriesPreferenceSetWorkflowCategorySettingObject]

Channels: TypeAlias = Union[bool, PreferenceSetChannelSettingParam]

WorkflowsPreferenceSetWorkflowCategorySettingObjectChannels: TypeAlias = Union[bool, PreferenceSetChannelSettingParam]


class WorkflowsPreferenceSetWorkflowCategorySettingObject(TypedDict, total=False):
    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences."""

    channels: Optional[Dict[str, WorkflowsPreferenceSetWorkflowCategorySettingObjectChannels]]
    """Channel preferences."""

    conditions: Optional[Iterable[Condition]]
    """A list of conditions to apply to a channel type."""


Workflows: TypeAlias = Union[bool, WorkflowsPreferenceSetWorkflowCategorySettingObject]
