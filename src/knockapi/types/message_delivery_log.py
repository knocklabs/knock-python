# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageDeliveryLog", "Request", "Response"]


class Request(BaseModel):
    body: Union[str, Dict[str, object], None] = None

    headers: Optional[Dict[str, object]] = None

    host: Optional[str] = None

    method: Optional[Literal["GET", "POST", "PUT", "DELETE", "PATCH"]] = None

    path: Optional[str] = None

    query: Optional[str] = None


class Response(BaseModel):
    body: Union[str, Dict[str, object], None] = None

    headers: Optional[Dict[str, object]] = None

    status: Optional[int] = None


class MessageDeliveryLog(BaseModel):
    id: str

    api_typename: str = FieldInfo(alias="__typename")

    environment_id: str

    inserted_at: str

    request: Request
    """A message delivery log request"""

    response: Response
    """A message delivery log response"""

    service_name: str
