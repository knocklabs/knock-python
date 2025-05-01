# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MsTeamListChannelsParams", "QueryOptions"]


class MsTeamListChannelsParams(TypedDict, total=False):
    ms_teams_tenant_object: Required[str]
    """A JSON encoded string containing the Microsoft Teams tenant object reference."""

    team_id: Required[str]
    """Microsoft Teams team ID."""

    query_options: QueryOptions


class QueryOptions(TypedDict, total=False):
    filter: Annotated[str, PropertyInfo(alias="$filter")]
    """
    [OData param](https://learn.microsoft.com/en-us/graph/query-parameters) passed
    to the Microsoft Graph API to filter channels.
    """

    select: Annotated[str, PropertyInfo(alias="$select")]
    """
    [OData param](https://learn.microsoft.com/en-us/graph/query-parameters) passed
    to the Microsoft Graph API to select specific properties.
    """
