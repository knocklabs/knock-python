# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .recipient_reference_param import RecipientReferenceParam

__all__ = ["WorkflowRecipientRunListParams"]


class WorkflowRecipientRunListParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after."""

    before: str
    """The cursor to fetch entries before."""

    ending_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Limits the results to workflow recipient runs started before the given date."""

    has_errors: bool
    """Limits the results to workflow recipient runs that have errors."""

    page_size: int
    """The number of items per page (defaults to 50)."""

    recipient: RecipientReferenceParam
    """Limits the results to workflow recipient runs for the given recipient.

    Accepts a user ID string or an object reference with `id` and `collection`.
    """

    starting_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Limits the results to workflow recipient runs started after the given date."""

    status: List[Literal["queued", "processing", "paused", "completed", "cancelled"]]
    """Limits the results to workflow recipient runs with the given status."""

    tenant: str
    """Limits the results to workflow recipient runs for the given tenant."""

    workflow: str
    """Limits the results to workflow recipient runs for the given workflow key."""
