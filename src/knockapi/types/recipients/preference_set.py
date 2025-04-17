# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.condition import Condition
from .preference_set_channel_types import PreferenceSetChannelTypes

__all__ = [
    "PreferenceSet",
    "Categories",
    "CategoriesPreferenceSetWorkflowCategorySettingObject",
    "Workflows",
    "WorkflowsPreferenceSetWorkflowCategorySettingObject",
]


class CategoriesPreferenceSetWorkflowCategorySettingObject(BaseModel):
    channel_types: Optional[PreferenceSetChannelTypes] = None
    """Channel type preferences."""

    conditions: Optional[List[Condition]] = None
    """A list of conditions to apply to a channel type."""


Categories: TypeAlias = Union[bool, CategoriesPreferenceSetWorkflowCategorySettingObject]


class WorkflowsPreferenceSetWorkflowCategorySettingObject(BaseModel):
    channel_types: Optional[PreferenceSetChannelTypes] = None
    """Channel type preferences."""

    conditions: Optional[List[Condition]] = None
    """A list of conditions to apply to a channel type."""


Workflows: TypeAlias = Union[bool, WorkflowsPreferenceSetWorkflowCategorySettingObject]


class PreferenceSet(BaseModel):
    id: str
    """Unique identifier for the preference set."""

    api_typename: str = FieldInfo(alias="__typename")
    """The type name of the schema."""

    categories: Optional[Dict[str, Categories]] = None
    """
    A setting for a preference set, where the key in the object is the category, and
    the values are the preference settings for that category.
    """

    channel_types: Optional[PreferenceSetChannelTypes] = None
    """Channel type preferences."""

    workflows: Optional[Dict[str, Workflows]] = None
    """
    A setting for a preference set, where the key in the object is the workflow key,
    and the values are the preference settings for that workflow.
    """
