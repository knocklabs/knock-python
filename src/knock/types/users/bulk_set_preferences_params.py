# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from ..preference_set_request_param import PreferenceSetRequestParam

__all__ = ["BulkSetPreferencesParams"]


class BulkSetPreferencesParams(TypedDict, total=False):
    preferences: Required[PreferenceSetRequestParam]
    """Set preferences for a recipient"""

    user_ids: Required[List[str]]
