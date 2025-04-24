# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .inline_identify_user_request_param import InlineIdentifyUserRequestParam

__all__ = ["AudienceAddMembersParams", "Member"]


class AudienceAddMembersParams(TypedDict, total=False):
    members: Required[Iterable[Member]]
    """A list of audience members to add."""


class Member(TypedDict, total=False):
    user: Required[InlineIdentifyUserRequestParam]
    """A set of parameters to inline-identify a user with.

    Inline identifying the user will ensure that the user is available before the
    request is executed in Knock. It will perform an upsert for the user you're
    supplying, replacing any properties specified.
    """

    tenant: Optional[str]
    """The unique identifier for the tenant."""
