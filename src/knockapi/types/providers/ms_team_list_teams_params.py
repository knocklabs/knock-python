# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MsTeamListTeamsParams", "QueryOptions"]


class MsTeamListTeamsParams(TypedDict, total=False):
    ms_teams_tenant_object: Required[str]
    """A JSON encoded string containing the Microsoft Teams tenant object reference."""

    query_options: QueryOptions


class QueryOptions(TypedDict, total=False):
    filter: Annotated[str, PropertyInfo(alias="$filter")]
    """
    [OData param](https://learn.microsoft.com/en-us/graph/query-parameters) passed
    to the Microsoft Graph API to filter teams.
    """

    select: Annotated[str, PropertyInfo(alias="$select")]
    """
    [OData param](https://learn.microsoft.com/en-us/graph/query-parameters) passed
    to the Microsoft Graph API to select fields on a team.
    """

    skiptoken: Annotated[str, PropertyInfo(alias="$skiptoken")]
    """
    [OData param](https://learn.microsoft.com/en-us/graph/query-parameters) passed
    to the Microsoft Graph API to retrieve the next page of results.
    """

    top: Annotated[int, PropertyInfo(alias="$top")]
    """
    [OData param](https://learn.microsoft.com/en-us/graph/query-parameters) passed
    to the Microsoft Graph API to limit the number of teams returned.
    """
