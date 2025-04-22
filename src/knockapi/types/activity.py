# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .recipient import Recipient

__all__ = ["Activity"]


class Activity(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the activity."""

    api_typename: Optional[str] = FieldInfo(alias="__typename", default=None)
    """The typename of the schema."""

    actor: Optional[Recipient] = None
    """A recipient of a notification, which is either a user or an object."""

    data: Optional[Dict[str, object]] = None
    """The workflow trigger `data` payload associated with the activity."""

    inserted_at: Optional[datetime] = None
    """Timestamp when the activity was created."""

    recipient: Optional[Recipient] = None
    """A recipient of a notification, which is either a user or an object."""

    updated_at: Optional[datetime] = None
    """Timestamp when the activity was last updated."""
