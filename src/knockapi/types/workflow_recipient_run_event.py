# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WorkflowRecipientRunEvent"]


class WorkflowRecipientRunEvent(BaseModel):
    """An event that occurred during a workflow recipient run."""

    id: str
    """The unique identifier for the event."""

    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    event: str
    """The type of event that occurred."""

    inserted_at: datetime
    """Timestamp when the resource was created."""

    status: Literal["ok", "error"]
    """Whether the event represents a successful or error state."""

    attempt: Optional[int] = None
    """The attempt number of the workflow recipient run event.

    Increments for each retry.
    """

    data: Optional[Dict[str, object]] = None
    """Event-specific data associated with the event."""

    step_ref: Optional[str] = None
    """The reference of the workflow step associated with this event."""

    step_type: Optional[str] = None
    """The type of workflow step associated with this event."""
