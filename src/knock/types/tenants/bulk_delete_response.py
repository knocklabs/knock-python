# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BulkDeleteResponse", "ErrorItem"]


class ErrorItem(BaseModel):
    id: str

    collection: Optional[str] = None


class BulkDeleteResponse(BaseModel):
    id: str

    api_typename: str = FieldInfo(alias="__typename")

    estimated_total_rows: int

    inserted_at: datetime

    name: str

    processed_rows: int

    status: Literal["queued", "processing", "completed", "failed"]

    success_count: int

    updated_at: datetime

    completed_at: Optional[datetime] = None

    error_count: Optional[int] = None

    error_items: Optional[List[ErrorItem]] = None
    """A list of items that failed to be processed"""

    failed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None
