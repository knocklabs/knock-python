# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["WorkflowTriggerResponse"]


class WorkflowTriggerResponse(BaseModel):
    workflow_run_id: str
    """The ID of the workflow trigger.

    This value allows you to track individual workflow runs associated with this
    trigger request.
    """
