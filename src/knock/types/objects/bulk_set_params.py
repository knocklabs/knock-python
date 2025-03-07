# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..shared_params.inline_object_request import InlineObjectRequest

__all__ = ["BulkSetParams"]


class BulkSetParams(TypedDict, total=False):
    objects: Required[Iterable[InlineObjectRequest]]
