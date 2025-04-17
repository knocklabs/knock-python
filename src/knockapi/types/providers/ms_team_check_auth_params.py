# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MsTeamCheckAuthParams"]


class MsTeamCheckAuthParams(TypedDict, total=False):
    ms_teams_tenant_object: Required[str]
    """A JSON encoded string containing the Microsoft Teams tenant object reference."""
