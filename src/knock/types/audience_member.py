# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .user import User
from .._models import BaseModel

__all__ = ["AudienceMember"]


class AudienceMember(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    added_at: datetime

    user: User
    """A user object"""

    user_id: str

    tenant: Optional[str] = None
