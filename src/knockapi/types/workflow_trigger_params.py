# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Required, TypedDict

from .recipient_request_param import RecipientRequestParam
from .inline_tenant_request_param import InlineTenantRequestParam

__all__ = ["WorkflowTriggerParams"]


class WorkflowTriggerParams(TypedDict, total=False):
    recipients: Required[List[RecipientRequestParam]]
    """The recipients to trigger the workflow for.

    Can inline identify users, objects, or use a list of user IDs. Limited to 1,000
    recipients.
    """

    actor: Optional[RecipientRequestParam]
    """Specifies a recipient in a request.

    This can either be a user identifier (string), an inline user request (object),
    or an inline object request, which is determined by the presence of a
    `collection` property.
    """

    cancellation_key: Optional[str]
    """
    An optional key that is used to reference a specific workflow trigger request
    when issuing a [workflow cancellation](/send-notifications/canceling-workflows)
    request. Must be provided while triggering a workflow in order to enable
    subsequent cancellation. Should be unique across trigger requests to avoid
    unintentional cancellations.
    """

    data: Optional[Dict[str, object]]
    """An optional map of data to pass into the workflow execution.

    There is a 1024 byte limit on the size of any single string value (with the
    exception of [email attachments](/integrations/email/attachments)), and a 10MB
    limit on the size of the full `data` payload.
    """

    tenant: Optional[InlineTenantRequestParam]
    """An request to set a tenant inline."""
