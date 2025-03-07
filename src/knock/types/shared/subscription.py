# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .object import Object
from ..._models import BaseModel
from .recipient import Recipient

__all__ = ["Subscription"]


class Subscription(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    inserted_at: datetime

    object: Object
    """A custom-object entity which belongs to a collection."""

    recipient: Recipient
    """A recipient, which is either a user or an object"""

    updated_at: datetime

    properties: Optional[Dict[str, builtins.object]] = None
    """The custom properties associated with the subscription"""
