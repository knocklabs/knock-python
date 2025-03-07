# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .shared_params.inline_identify_user_request import InlineIdentifyUserRequest

__all__ = ["AudienceRemoveMembersParams", "Member"]


class AudienceRemoveMembersParams(TypedDict, total=False):
    members: Required[Iterable[Member]]


class Member(TypedDict, total=False):
    user: Required[InlineIdentifyUserRequest]
    """A set of parameters to inline-identify a user with.

    Inline identifying the user will ensure that the user is available before the
    request is executed in Knock. It will perform an upsert against the user you're
    supplying, replacing any properties specified.
    """

    tenant: Optional[str]
