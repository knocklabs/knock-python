# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.condition import Condition
from .preference_set_channel_types_param import PreferenceSetChannelTypesParam

__all__ = [
    "PreferenceSetRequestParam",
    "Categories",
    "CategoriesPreferenceSetWorkflowCategorySettingObject",
    "Workflows",
    "WorkflowsPreferenceSetWorkflowCategorySettingObject",
]


class CategoriesPreferenceSetWorkflowCategorySettingObject(TypedDict, total=False):
    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences."""

    conditions: Optional[Iterable[Condition]]
    """A list of conditions to apply to a channel type."""


Categories: TypeAlias = Union[bool, CategoriesPreferenceSetWorkflowCategorySettingObject]


class WorkflowsPreferenceSetWorkflowCategorySettingObject(TypedDict, total=False):
    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences."""

    conditions: Optional[Iterable[Condition]]
    """A list of conditions to apply to a channel type."""


Workflows: TypeAlias = Union[bool, WorkflowsPreferenceSetWorkflowCategorySettingObject]


class PreferenceSetRequestParam(TypedDict, total=False):
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

    commercial_subscribed: Optional[bool]
    """Whether the recipient is subscribed to commercial communications.

    When false, the recipient will not receive commercial workflow notifications.
    """

    workflows: Optional[Dict[str, Workflows]]
    """
    An object where the key is the workflow key and the values are the preference
    settings for that workflow.
    """
