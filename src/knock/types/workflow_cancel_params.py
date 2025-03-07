# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["WorkflowCancelParams"]


class WorkflowCancelParams(TypedDict, total=False):
    cancellation_key: Required[str]
    """
    The cancellation key supplied to the workflow trigger endpoint to use for
    cancelling one or more workflow runs.
    """

    recipients: Optional[List[str]]
    """
    An optional list of recipients to cancel the workflow for using the cancellation
    key.
    """

    tenant: Optional[str]
