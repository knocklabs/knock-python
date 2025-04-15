# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SlackListChannelsParams", "QueryOptions"]


class SlackListChannelsParams(TypedDict, total=False):
    access_token_object: Required[str]
    """A JSON encoded string containing the access token object reference"""

    query_options: QueryOptions


class QueryOptions(TypedDict, total=False):
    cursor: str
    """A cursor to paginate through the channels"""

    exclude_archived: str
    """Whether to exclude archived channels"""

    limit: str
    """The number of channels to return"""

    team_id: str
    """The ID of the Slack team to get channels for"""

    types: str
    """The types of channels to return"""
