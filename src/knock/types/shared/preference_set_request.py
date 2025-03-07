# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .condition import Condition
from .preference_set_channel_types import PreferenceSetChannelTypes

__all__ = [
    "PreferenceSetRequest",
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


class PreferenceSetRequest(BaseModel):
    categories: Optional[Dict[str, Categories]] = None
    """
    A setting for a preference set, where the key in the object is the category, and
    the values are the preference settings for that category.
    """

    channel_types: Optional[PreferenceSetChannelTypes] = None
    """Channel type preferences"""

    workflows: Optional[Dict[str, Workflows]] = None
    """
    A setting for a preference set, where the key in the object is the workflow key,
    and the values are the preference settings for that workflow.
    """
