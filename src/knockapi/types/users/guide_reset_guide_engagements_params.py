# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GuideResetGuideEngagementsParams"]


class GuideResetGuideEngagementsParams(TypedDict, total=False):
    guide_key: Required[str]
    """The key of the guide."""

    tenant: str
    """The tenant ID of the guide."""
