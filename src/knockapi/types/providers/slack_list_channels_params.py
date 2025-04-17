# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SlackListChannelsParams", "QueryOptions"]


class SlackListChannelsParams(TypedDict, total=False):
    access_token_object: Required[str]
    """A JSON encoded string containing the access token object reference."""

    query_options: QueryOptions


class QueryOptions(TypedDict, total=False):
    cursor: str
    """
    Paginate through collections of data by setting the cursor parameter to a
    next_cursor attribute returned by a previous request's response_metadata.
    Default value fetches the first "page" of the collection.
    """

    exclude_archived: bool
    """Set to true to exclude archived channels from the list."""

    limit: int
    """The maximum number of channels to return."""

    team_id: str
    """Encoded team ID (T1234) to list channels in, required if org token is used."""

    types: str
    """
    Mix and match channel types by providing a comma-separated list of any
    combination of public_channel, private_channel, mpim, im.
    """
