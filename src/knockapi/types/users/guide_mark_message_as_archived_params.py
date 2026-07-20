# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GuideMarkMessageAsArchivedParams"]


class GuideMarkMessageAsArchivedParams(TypedDict, total=False):
    channel_id: Required[str]
    """The unique identifier for the channel."""

    guide_id: Required[str]
    """The unique identifier for the guide."""

    guide_key: Required[str]
    """The key of the guide."""

    guide_step_ref: Required[str]
    """The step reference of the guide."""

    is_final: bool
    """Whether the guide is final."""

    tenant: str
    """The tenant ID of the guide."""

    unthrottled: bool
    """Whether the guide bypasses its guide group's throttle settings.

    When true, archiving the guide does not open a new throttle window.
    """
