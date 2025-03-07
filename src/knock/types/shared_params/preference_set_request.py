# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import TypeAlias, TypedDict

from .condition import Condition
from .preference_set_channel_types import PreferenceSetChannelTypes

__all__ = [
    "PreferenceSetRequest",
    "Categories",
    "CategoriesPreferenceSetWorkflowCategorySettingObject",
    "Workflows",
    "WorkflowsPreferenceSetWorkflowCategorySettingObject",
]


class CategoriesPreferenceSetWorkflowCategorySettingObject(TypedDict, total=False):
    channel_types: Optional[PreferenceSetChannelTypes]
    """Channel type preferences"""

    conditions: Optional[Iterable[Condition]]


Categories: TypeAlias = Union[bool, CategoriesPreferenceSetWorkflowCategorySettingObject]


class WorkflowsPreferenceSetWorkflowCategorySettingObject(TypedDict, total=False):
    channel_types: Optional[PreferenceSetChannelTypes]
    """Channel type preferences"""

    conditions: Optional[Iterable[Condition]]


Workflows: TypeAlias = Union[bool, WorkflowsPreferenceSetWorkflowCategorySettingObject]


class PreferenceSetRequest(TypedDict, total=False):
    categories: Optional[Dict[str, Categories]]
    """
    A setting for a preference set, where the key in the object is the category, and
    the values are the preference settings for that category.
    """

    channel_types: Optional[PreferenceSetChannelTypes]
    """Channel type preferences"""

    workflows: Optional[Dict[str, Workflows]]
    """
    A setting for a preference set, where the key in the object is the workflow key,
    and the values are the preference settings for that workflow.
    """
