# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.condition import Condition
from .preference_set_channel_types import PreferenceSetChannelTypes

__all__ = ["PreferenceSet", "Categories", "CategoriesUnionMember1", "Workflows", "WorkflowsUnionMember1"]


class CategoriesUnionMember1(BaseModel):
    channel_types: Optional[PreferenceSetChannelTypes] = None
    """Channel type preferences"""

    conditions: Optional[List[Condition]] = None


Categories: TypeAlias = Union[bool, CategoriesUnionMember1]


class WorkflowsUnionMember1(BaseModel):
    channel_types: Optional[PreferenceSetChannelTypes] = None
    """Channel type preferences"""

    conditions: Optional[List[Condition]] = None


Workflows: TypeAlias = Union[bool, WorkflowsUnionMember1]


class PreferenceSet(BaseModel):
    id: str

    api_typename: str = FieldInfo(alias="__typename")

    categories: Optional[Dict[str, Categories]] = None

    channel_types: Optional[PreferenceSetChannelTypes] = None
    """Channel type preferences"""

    workflows: Optional[Dict[str, Workflows]] = None
