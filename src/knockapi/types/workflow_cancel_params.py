# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["WorkflowCancelParams"]


class WorkflowCancelParams(TypedDict, total=False):
    cancellation_key: Required[str]
    """The cancellation key provided during the initial notify call.

    If used in a cancel request, will cancel the notification for the recipients
    specified in the cancel request.
    """

    recipients: Optional[List[str]]
    """A list of recipients to cancel the notification for.

    If omitted, cancels for all recipients associated with the cancellation key.
    """

    tenant: Optional[str]
    """The unique identifier for the tenant."""
