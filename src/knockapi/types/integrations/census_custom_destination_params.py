# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CensusCustomDestinationParams"]


class CensusCustomDestinationParams(TypedDict, total=False):
    id: Required[str]
    """The unique identifier for the RPC request."""

    jsonrpc: Required[str]
    """The JSON-RPC version."""

    method: Required[str]
    """The method name to execute."""

    params: object
    """The parameters for the method."""
