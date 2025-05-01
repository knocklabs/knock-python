# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BulkOperation", "ErrorItem"]


class ErrorItem(BaseModel):
    id: str
    """Unique identifier for the object."""

    collection: Optional[str] = None
    """The collection this object belongs to."""


class BulkOperation(BaseModel):
    id: str
    """Unique identifier for the bulk operation."""

    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    estimated_total_rows: int
    """The estimated total number of rows to process."""

    inserted_at: datetime
    """Timestamp when the resource was created."""

    name: str
    """The name of the bulk operation."""

    processed_rows: int
    """The number of rows processed so far."""

    status: Literal["queued", "processing", "completed", "failed"]
    """The status of the bulk operation."""

    success_count: int
    """The number of successful operations."""

    updated_at: datetime
    """The timestamp when the resource was last updated."""

    completed_at: Optional[datetime] = None
    """Timestamp when the bulk operation was completed."""

    error_count: Optional[int] = None
    """The number of failed operations."""

    error_items: Optional[List[ErrorItem]] = None
    """A list of items that failed to be processed."""

    failed_at: Optional[datetime] = None
    """Timestamp when the bulk operation failed."""

    progress_path: Optional[str] = None
    """The URI to the bulk operation's progress."""

    started_at: Optional[datetime] = None
    """Timestamp when the bulk operation was started."""
