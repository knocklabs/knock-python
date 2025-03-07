# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params.condition import Condition
from .preference_set_channel_types_param import PreferenceSetChannelTypesParam

__all__ = [
    "ObjectSetPreferencesParams",
    "Categories",
    "CategoriesPreferenceSetWorkflowCategorySettingObject",
    "Workflows",
    "WorkflowsPreferenceSetWorkflowCategorySettingObject",
]


class ObjectSetPreferencesParams(TypedDict, total=False):
    collection: Required[str]

    object_id: Required[str]

    categories: Optional[Dict[str, Categories]]
    """
    A setting for a preference set, where the key in the object is the category, and
    the values are the preference settings for that category.
    """

    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences"""

    workflows: Optional[Dict[str, Workflows]]
    """
    A setting for a preference set, where the key in the object is the workflow key,
    and the values are the preference settings for that workflow.
    """


class CategoriesPreferenceSetWorkflowCategorySettingObject(TypedDict, total=False):
    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences"""

    conditions: Optional[Iterable[Condition]]


Categories: TypeAlias = Union[bool, CategoriesPreferenceSetWorkflowCategorySettingObject]


class WorkflowsPreferenceSetWorkflowCategorySettingObject(TypedDict, total=False):
    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences"""

    conditions: Optional[Iterable[Condition]]


Workflows: TypeAlias = Union[bool, WorkflowsPreferenceSetWorkflowCategorySettingObject]
