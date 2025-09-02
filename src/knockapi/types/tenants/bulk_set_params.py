# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from ..inline_tenant_request_param import InlineTenantRequestParam

__all__ = ["BulkSetParams"]


class BulkSetParams(TypedDict, total=False):
    tenants: Required[SequenceNotStr[InlineTenantRequestParam]]
    """The tenants to be upserted."""
