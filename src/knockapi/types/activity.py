# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .recipient import Recipient

__all__ = ["Activity"]


class Activity(BaseModel):
    id: Optional[str] = None

    api_typename: Optional[str] = FieldInfo(alias="__typename", default=None)

    actor: Optional[Recipient] = None
    """A recipient, which is either a user or an object"""

    data: Optional[object] = None
    """The data associated with the activity"""

    inserted_at: Optional[datetime] = None

    recipient: Optional[Recipient] = None
    """A recipient, which is either a user or an object"""

    updated_at: Optional[datetime] = None
