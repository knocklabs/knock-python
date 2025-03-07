# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from ..shared_params.inline_tenant_request import InlineTenantRequest

__all__ = ["BulkSetParams"]


class BulkSetParams(TypedDict, total=False):
    tenants: Required[List[InlineTenantRequest]]
