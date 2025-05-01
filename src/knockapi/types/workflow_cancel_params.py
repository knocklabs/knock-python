# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

from .recipient_reference_param import RecipientReferenceParam

__all__ = ["WorkflowCancelParams"]


class WorkflowCancelParams(TypedDict, total=False):
    cancellation_key: Required[str]
    """
    An optional key that is used to reference a specific workflow trigger request
    when issuing a [workflow cancellation](/send-notifications/canceling-workflows)
    request. Must be provided while triggering a workflow in order to enable
    subsequent cancellation. Should be unique across trigger requests to avoid
    unintentional cancellations.
    """

    recipients: Optional[List[RecipientReferenceParam]]
    """A list of recipients to cancel the notification for.

    If omitted, cancels for all recipients associated with the cancellation key.
    """
