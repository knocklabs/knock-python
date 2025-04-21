# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import TypeAlias, TypedDict

from .condition_param import ConditionParam
from .recipients.preference_set_channel_types_param import PreferenceSetChannelTypesParam

__all__ = [
    "ObjectSetPreferencesParams",
    "Categories",
    "CategoriesPreferenceSetWorkflowCategorySettingObject",
    "Workflows",
    "WorkflowsPreferenceSetWorkflowCategorySettingObject",
]


class ObjectSetPreferencesParams(TypedDict, total=False):
    categories: Optional[Dict[str, Categories]]
    """
    An object where the key is the category and the values are the preference
    settings for that category.
    """

    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences."""

    workflows: Optional[Dict[str, Workflows]]
    """
    An object where the key is the workflow key and the values are the preference
    settings for that workflow.
    """


class CategoriesPreferenceSetWorkflowCategorySettingObject(TypedDict, total=False):
    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences."""

    conditions: Optional[Iterable[ConditionParam]]
    """A list of conditions to apply to a channel type."""


Categories: TypeAlias = Union[bool, CategoriesPreferenceSetWorkflowCategorySettingObject]


class WorkflowsPreferenceSetWorkflowCategorySettingObject(TypedDict, total=False):
    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences."""

    conditions: Optional[Iterable[ConditionParam]]
    """A list of conditions to apply to a channel type."""


Workflows: TypeAlias = Union[bool, WorkflowsPreferenceSetWorkflowCategorySettingObject]
