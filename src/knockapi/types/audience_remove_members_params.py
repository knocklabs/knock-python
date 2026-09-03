# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .audience_member_request_param import AudienceMemberRequestParam

__all__ = ["AudienceRemoveMembersParams"]


class AudienceRemoveMembersParams(TypedDict, total=False):
    members: Required[Iterable[AudienceMemberRequestParam]]
    """A list of audience members to remove.

    You can remove up to 1,000 members per request.
    """
