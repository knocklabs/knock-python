# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .recipient_reference import RecipientReference

__all__ = ["WorkflowRecipientRun", "TriggerSource"]


class TriggerSource(BaseModel):
    """Describes how the workflow was triggered."""

    type: Literal["api", "audience", "schedule", "broadcast", "workflow_step", "integration", "rehearsal"]
    """The type of trigger source.

    One of `api`, `audience`, `schedule`, `broadcast`, `workflow_step`,
    `integration`, or `rehearsal`.
    """

    audience_key: Optional[str] = None
    """The key of the audience that triggered the workflow."""

    cancellation_key: Optional[str] = None
    """The cancellation key provided when the workflow was triggered via the API."""

    schedule_id: Optional[str] = None
    """The ID of the schedule that triggered the workflow."""


class WorkflowRecipientRun(BaseModel):
    """
    A workflow recipient run represents an individual execution of a workflow for a specific recipient.
    """

    id: str
    """The unique identifier for the workflow recipient run (per-recipient)."""

    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    inserted_at: datetime
    """Timestamp when the resource was created."""

    recipient: RecipientReference
    """
    A reference to a recipient, either a user identifier (string) or an object
    reference (ID, collection).
    """

    status: Literal["queued", "processing", "paused", "completed", "cancelled"]
    """The current status of the workflow recipient run.

    One of `queued`, `processing`, `paused`, `completed`, or `cancelled`.
    """

    trigger_source: TriggerSource
    """Describes how the workflow was triggered."""

    updated_at: datetime
    """The timestamp when the resource was last updated."""

    workflow: str
    """The key of the workflow that was executed."""

    workflow_run_id: str
    """
    The identifier for the top-level workflow run shared across all recipients in a
    single trigger.
    """

    actor: Optional[RecipientReference] = None
    """
    A reference to a recipient, either a user identifier (string) or an object
    reference (ID, collection).
    """

    error_count: Optional[int] = None
    """The number of errors encountered during the workflow recipient run."""

    tenant: Optional[str] = None
    """The tenant associated with the workflow recipient run."""
