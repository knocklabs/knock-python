# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .workflow_recipient_run import WorkflowRecipientRun
from .workflow_recipient_run_event import WorkflowRecipientRunEvent

__all__ = ["WorkflowRecipientRunDetail"]


class WorkflowRecipientRunDetail(WorkflowRecipientRun):
    """A single workflow recipient run with its events."""

    events: List[WorkflowRecipientRunEvent]
    """A list of events that occurred during the workflow recipient run."""
