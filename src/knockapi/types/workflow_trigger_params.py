# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import TypedDict

from .recipient_request_param import RecipientRequestParam
from .inline_tenant_request_param import InlineTenantRequestParam

__all__ = ["WorkflowTriggerParams"]


class WorkflowTriggerParams(TypedDict, total=False):
    actor: Optional[RecipientRequestParam]
    """Specifies a recipient in a request.

    This can either be a user identifier (string), an inline user request (object),
    or an inline object request, which is determined by the presence of a
    `collection` property.
    """

    cancellation_key: Optional[str]
    """
    An optional key that is used in the workflow cancellation endpoint to target a
    cancellation of any workflow runs associated with this trigger.
    """

    data: Optional[Dict[str, object]]
    """An optional map of data to be used in the workflow.

    This data will be available to the workflow as a map in the `data` field.
    """

    recipients: List[RecipientRequestParam]
    """The recipients to trigger the workflow for.

    Cannot exceed 1000 recipients in a single trigger.
    """

    tenant: Optional[InlineTenantRequestParam]
    """An inline tenant request"""
