# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["FeedListItemsParams"]


class FeedListItemsParams(TypedDict, total=False):
    after: str
    """The cursor to fetch entries after."""

    archived: Literal["exclude", "include", "only"]
    """The archived status of the feed items."""

    before: str
    """The cursor to fetch entries before."""

    exclude: str
    """Comma-separated list of field paths to exclude from the response.

    Use dot notation for nested fields (e.g., `entries.archived_at`). Limited to 3
    levels deep.
    """

    has_tenant: bool
    """Whether the feed items have a tenant."""

    locale: str
    """The locale to render the feed items in.

    Must be in the IETF 5646 format (e.g. `en-US`). When not provided, will default
    to the locale that the feed items were rendered in. Only available for
    enterprise plan customers using custom translations.
    """

    mode: Literal["compact", "rich"]
    """The mode to render the feed items in.

    Can be `compact` or `rich`. Defaults to `rich`. When `mode` is `compact`, feed
    items will not have `activities` and `total_activities` fields, and the `data`
    field will not include nested arrays and objects.
    """

    page_size: int
    """The number of items per page (defaults to 50)."""

    source: str
    """The workflow key associated with the message in the feed."""

    status: Literal["unread", "read", "unseen", "seen", "all"]
    """The status of the feed items."""

    tenant: str
    """The tenant associated with the feed items."""

    trigger_data: str
    """The trigger data of the feed items (as a JSON string)."""

    workflow_categories: SequenceNotStr[str]
    """The workflow categories of the feed items."""
