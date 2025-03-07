# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Tenant"]


class Tenant(BaseModel):
    id: str

    api_typename: str = FieldInfo(alias="__typename")

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
