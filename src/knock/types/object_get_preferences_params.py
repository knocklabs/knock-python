# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ObjectGetPreferencesParams"]


class ObjectGetPreferencesParams(TypedDict, total=False):
    collection: Required[str]

    object_id: Required[str]

    tenant: str
    """Tenant ID"""
