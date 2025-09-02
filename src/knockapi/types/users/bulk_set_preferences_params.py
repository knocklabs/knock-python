# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from ..recipients.preference_set_request_param import PreferenceSetRequestParam

__all__ = ["BulkSetPreferencesParams"]


class BulkSetPreferencesParams(TypedDict, total=False):
    preferences: Required[PreferenceSetRequestParam]
    """A request to set a preference set for a recipient."""

    user_ids: Required[SequenceNotStr[str]]
    """A list of user IDs."""
