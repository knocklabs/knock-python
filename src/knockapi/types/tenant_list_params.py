# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TenantListParams"]


class TenantListParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    name: str
    """Filter tenants by name."""

    page_size: int
    """The number of items per page."""

    tenant_id: str
    """Filter tenants by ID."""
