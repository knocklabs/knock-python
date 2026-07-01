# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..shared_params.condition import Condition
from ..recipients.preference_set_channel_types_param import PreferenceSetChannelTypesParam
from ..recipients.preference_set_channel_setting_param import PreferenceSetChannelSettingParam

__all__ = [
    "BulkSetPreferencesParams",
    "Preferences",
    "PreferencesCategories",
    "PreferencesCategoriesPreferenceSetWorkflowCategorySettingObject",
    "PreferencesCategoriesPreferenceSetWorkflowCategorySettingObjectChannels",
    "PreferencesChannels",
    "PreferencesWorkflows",
    "PreferencesWorkflowsPreferenceSetWorkflowCategorySettingObject",
    "PreferencesWorkflowsPreferenceSetWorkflowCategorySettingObjectChannels",
]


class BulkSetPreferencesParams(TypedDict, total=False):
    preferences: Required[Preferences]
    """A preference set to apply in a bulk operation.

    Always replaces existing preferences for the specified set.
    """

    user_ids: Required[SequenceNotStr[str]]
    """A list of user IDs."""


PreferencesCategoriesPreferenceSetWorkflowCategorySettingObjectChannels: TypeAlias = Union[
    bool, PreferenceSetChannelSettingParam
]


class PreferencesCategoriesPreferenceSetWorkflowCategorySettingObject(TypedDict, total=False):
    """
    The settings object for a workflow or category, where you can specify channel types or conditions.
    """

    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences."""

    channels: Optional[Dict[str, PreferencesCategoriesPreferenceSetWorkflowCategorySettingObjectChannels]]
    """Channel preferences."""

    conditions: Optional[Iterable[Condition]]
    """A list of conditions to apply to a channel type."""


PreferencesCategories: TypeAlias = Union[bool, PreferencesCategoriesPreferenceSetWorkflowCategorySettingObject]

PreferencesChannels: TypeAlias = Union[bool, PreferenceSetChannelSettingParam]

PreferencesWorkflowsPreferenceSetWorkflowCategorySettingObjectChannels: TypeAlias = Union[
    bool, PreferenceSetChannelSettingParam
]


class PreferencesWorkflowsPreferenceSetWorkflowCategorySettingObject(TypedDict, total=False):
    """
    The settings object for a workflow or category, where you can specify channel types or conditions.
    """

    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences."""

    channels: Optional[Dict[str, PreferencesWorkflowsPreferenceSetWorkflowCategorySettingObjectChannels]]
    """Channel preferences."""

    conditions: Optional[Iterable[Condition]]
    """A list of conditions to apply to a channel type."""


PreferencesWorkflows: TypeAlias = Union[bool, PreferencesWorkflowsPreferenceSetWorkflowCategorySettingObject]


class Preferences(TypedDict, total=False):
    """A preference set to apply in a bulk operation.

    Always replaces existing preferences for the specified set.
    """

    id: str
    """Identifier for the preference set to update. Can be `default` or a tenant ID."""

    categories: Optional[Dict[str, PreferencesCategories]]
    """
    An object where the key is the category and the values are the preference
    settings for that category.
    """

    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences."""

    channels: Optional[Dict[str, PreferencesChannels]]
    """Channel preferences."""

    commercial_subscribed: Optional[bool]
    """Whether the recipient is subscribed to commercial communications.

    When false, the recipient will not receive commercial workflow notifications.
    """

    workflows: Optional[Dict[str, PreferencesWorkflows]]
    """
    An object where the key is the workflow key and the values are the preference
    settings for that workflow.
    """
