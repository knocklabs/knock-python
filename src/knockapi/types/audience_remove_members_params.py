# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AudienceRemoveMembersParams", "Member", "MemberUser"]


class AudienceRemoveMembersParams(TypedDict, total=False):
    members: Required[Iterable[Member]]
    """A list of audience members to remove."""


class MemberUser(TypedDict, total=False):
    id: str
    """The ID for the user that you set when identifying them in Knock."""


class Member(TypedDict, total=False):
    user: Required[MemberUser]
    """An object containing the user's ID."""

    tenant: Optional[str]
    """The unique identifier for the tenant."""
