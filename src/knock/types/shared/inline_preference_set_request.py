# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

from .preference_set_request import PreferenceSetRequest

__all__ = ["InlinePreferenceSetRequest"]

InlinePreferenceSetRequest: TypeAlias = Dict[str, PreferenceSetRequest]
