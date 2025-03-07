# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .condition import Condition
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
    """Channel type preferences"""

    conditions: Optional[List[Condition]] = None


Categories: TypeAlias = Union[bool, CategoriesPreferenceSetWorkflowCategorySettingObject]


class WorkflowsPreferenceSetWorkflowCategorySettingObject(BaseModel):
    channel_types: Optional[PreferenceSetChannelTypes] = None
    """Channel type preferences"""

    conditions: Optional[List[Condition]] = None


Workflows: TypeAlias = Union[bool, WorkflowsPreferenceSetWorkflowCategorySettingObject]


class PreferenceSet(BaseModel):
    id: str

    api_typename: str = FieldInfo(alias="__typename")

    categories: Optional[Dict[str, Categories]] = None
    """A map of categories and their settings"""

    channel_types: Optional[PreferenceSetChannelTypes] = None
    """Channel type preferences"""

    workflows: Optional[Dict[str, Workflows]] = None
    """A map of workflows and their settings"""
