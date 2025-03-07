# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    id: str

    api_typename: str = FieldInfo(alias="__typename")

    updated_at: datetime

    avatar: Optional[str] = None

    created_at: Optional[datetime] = None

    email: Optional[str] = None

    name: Optional[str] = None

    phone_number: Optional[str] = None

    timezone: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
