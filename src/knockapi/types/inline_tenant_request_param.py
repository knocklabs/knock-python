# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .tenant_request_param import TenantRequestParam

__all__ = ["InlineTenantRequestParam"]

InlineTenantRequestParam: TypeAlias = Union[str, TenantRequestParam]
