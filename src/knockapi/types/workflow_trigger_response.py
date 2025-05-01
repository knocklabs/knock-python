# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WorkflowTriggerResponse"]


class WorkflowTriggerResponse(BaseModel):
    workflow_run_id: str
    """
    This value allows you to track individual messages associated with this trigger
    request.
    """
