# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TenantGetParams"]


class TenantGetParams(TypedDict, total=False):
    resolve_full_preference_settings: bool
    """
    When true, merges environment-level default preferences into the tenant's
    `settings.preference_set` field before returning the response. Defaults to
    false.
    """
