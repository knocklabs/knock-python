# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from ..condition_param import ConditionParam
from .preference_set_channel_types_param import PreferenceSetChannelTypesParam

__all__ = [
    "InlinePreferenceSetRequestParam",
    "InlinePreferenceSetRequestParamItem",
    "InlinePreferenceSetRequestParamItemCategories",
    "InlinePreferenceSetRequestParamItemCategoriesPreferenceSetWorkflowCategorySettingObject",
    "InlinePreferenceSetRequestParamItemWorkflows",
    "InlinePreferenceSetRequestParamItemWorkflowsPreferenceSetWorkflowCategorySettingObject",
]


class InlinePreferenceSetRequestParamItemCategoriesPreferenceSetWorkflowCategorySettingObject(TypedDict, total=False):
    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences."""

    conditions: Optional[Iterable[ConditionParam]]
    """A list of conditions to apply to a channel type."""


InlinePreferenceSetRequestParamItemCategories: TypeAlias = Union[
    bool, InlinePreferenceSetRequestParamItemCategoriesPreferenceSetWorkflowCategorySettingObject
]


class InlinePreferenceSetRequestParamItemWorkflowsPreferenceSetWorkflowCategorySettingObject(TypedDict, total=False):
    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences."""

    conditions: Optional[Iterable[ConditionParam]]
    """A list of conditions to apply to a channel type."""


InlinePreferenceSetRequestParamItemWorkflows: TypeAlias = Union[
    bool, InlinePreferenceSetRequestParamItemWorkflowsPreferenceSetWorkflowCategorySettingObject
]


class InlinePreferenceSetRequestParamItem(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the preference set."""

    categories: Optional[Dict[str, InlinePreferenceSetRequestParamItemCategories]]
    """
    An object where the key is the category and the values are the preference
    settings for that category.
    """

    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences."""

    workflows: Optional[Dict[str, InlinePreferenceSetRequestParamItemWorkflows]]
    """
    An object where the key is the workflow key and the values are the preference
    settings for that workflow.
    """


InlinePreferenceSetRequestParam: TypeAlias = List[InlinePreferenceSetRequestParamItem]
