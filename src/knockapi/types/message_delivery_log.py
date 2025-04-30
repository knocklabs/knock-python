# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageDeliveryLog", "Request", "Response"]


class Request(BaseModel):
    body: Union[str, Dict[str, object], None] = None
    """The body content that was sent with the request."""

    headers: Optional[Dict[str, object]] = None
    """The headers that were sent with the request."""

    host: Optional[str] = None
    """The host to which the request was sent."""

    method: Optional[Literal["GET", "POST", "PUT", "DELETE", "PATCH"]] = None
    """The HTTP method used for the request."""

    path: Optional[str] = None
    """The path of the URL that was requested."""

    query: Optional[str] = None
    """The query string of the URL that was requested."""


class Response(BaseModel):
    body: Union[str, Dict[str, object], None] = None
    """The body content that was received with the response."""

    headers: Optional[Dict[str, object]] = None
    """The headers that were received with the response."""

    status: Optional[int] = None
    """The HTTP status code of the response."""


class MessageDeliveryLog(BaseModel):
    id: str
    """The unique identifier for the message delivery log."""

    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    environment_id: str
    """The ID of the environment in which the message delivery occurred."""

    inserted_at: str
    """Timestamp when the message delivery log was created."""

    request: Request
    """A message delivery log request."""

    response: Response
    """A message delivery log response."""

    service_name: str
    """The name of the service that processed the delivery."""
