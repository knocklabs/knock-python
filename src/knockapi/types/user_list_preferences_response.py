# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .recipients.preference_set import PreferenceSet

__all__ = ["UserListPreferencesResponse"]

UserListPreferencesResponse: TypeAlias = List[PreferenceSet]
