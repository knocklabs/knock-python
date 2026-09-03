# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .audience_member_request_param import AudienceMemberRequestParam

__all__ = ["AudienceAddMembersParams"]


class AudienceAddMembersParams(TypedDict, total=False):
    members: Required[Iterable[AudienceMemberRequestParam]]
    """A list of audience members to add. You can add up to 1,000 members per request."""

    create_audience: bool
    """Create the audience if it does not exist."""
