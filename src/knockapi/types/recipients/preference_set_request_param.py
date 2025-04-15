# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import TypeAlias, TypedDict

from ..shared_params.condition import Condition
from .preference_set_channel_types_param import PreferenceSetChannelTypesParam

__all__ = ["PreferenceSetRequestParam", "Categories", "CategoriesUnionMember1", "Workflows", "WorkflowsUnionMember1"]


class CategoriesUnionMember1(TypedDict, total=False):
    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences"""

    conditions: Iterable[Condition]


Categories: TypeAlias = Union[bool, CategoriesUnionMember1]


class WorkflowsUnionMember1(TypedDict, total=False):
    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences"""

    conditions: Iterable[Condition]


Workflows: TypeAlias = Union[bool, WorkflowsUnionMember1]


class PreferenceSetRequestParam(TypedDict, total=False):
    categories: Optional[Dict[str, Categories]]

    channel_types: Optional[PreferenceSetChannelTypesParam]
    """Channel type preferences"""

    workflows: Optional[Dict[str, Workflows]]
