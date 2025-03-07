# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from ..shared_params.preference_set_request import PreferenceSetRequest

__all__ = ["BulkSetPreferencesParams"]


class BulkSetPreferencesParams(TypedDict, total=False):
    preferences: Required[PreferenceSetRequest]
    """Set preferences for a recipient"""

    user_ids: Required[List[str]]
