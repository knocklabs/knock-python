# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from ..inline_tenant_request_param import InlineTenantRequestParam

__all__ = ["BulkSetParams"]


class BulkSetParams(TypedDict, total=False):
    tenants: Required[List[InlineTenantRequestParam]]
    """The tenants to be upserted."""
