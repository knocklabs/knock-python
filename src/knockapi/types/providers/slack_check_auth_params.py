# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SlackCheckAuthParams"]


class SlackCheckAuthParams(TypedDict, total=False):
    access_token_object: Required[str]
    """A JSON encoded string containing the access token object reference."""
