# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Condition"]


class Condition(BaseModel):
    argument: Optional[str] = None
    """The argument value to compare against in the condition."""

    operator: Literal[
        "equal_to",
        "not_equal_to",
        "greater_than",
        "less_than",
        "greater_than_or_equal_to",
        "less_than_or_equal_to",
        "contains",
        "not_contains",
        "empty",
        "not_empty",
        "contains_all",
        "is_timestamp",
        "is_not_timestamp",
        "is_timestamp_after",
        "is_timestamp_before",
        "is_timestamp_between",
        "is_audience_member",
        "is_not_audience_member",
    ]
    """The operator to use in the condition evaluation."""

    variable: str
    """The variable to be evaluated in the condition."""
