# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .tenant_request import TenantRequest

__all__ = ["InlineTenantRequest"]

InlineTenantRequest: TypeAlias = Union[str, TenantRequest]
