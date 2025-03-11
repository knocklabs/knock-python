# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "MessageGetContentResponse",
    "Data",
    "DataMessageEmailContent",
    "DataMessageSMSContent",
    "DataMessagePushContent",
    "DataMessageChatContent",
    "DataMessageChatContentTemplate",
    "DataMessageChatContentTemplateBlock",
    "DataMessageInAppFeedContent",
    "DataMessageInAppFeedContentBlock",
    "DataMessageInAppFeedContentBlockMessageInAppFeedContentBlock",
    "DataMessageInAppFeedContentBlockMessageInAppFeedButtonSetBlock",
    "DataMessageInAppFeedContentBlockMessageInAppFeedButtonSetBlockButton",
]


class DataMessageEmailContent(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    from_: str = FieldInfo(alias="from")

    html_body: str

    subject_line: str

    text_body: str

    to: str

    bcc: Optional[str] = None

    cc: Optional[str] = None

    reply_to: Optional[str] = None


class DataMessageSMSContent(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    body: str

    to: str


class DataMessagePushContent(BaseModel):
    token: str

    api_typename: str = FieldInfo(alias="__typename")

    body: str

    title: str

    data: Optional[Dict[str, object]] = None


class DataMessageChatContentTemplateBlock(BaseModel):
    content: str

    name: str

    type: Literal["text", "markdown"]


class DataMessageChatContentTemplate(BaseModel):
    blocks: Optional[List[DataMessageChatContentTemplateBlock]] = None
    """The structured blocks of the message"""

    json_content: Optional[Dict[str, object]] = None
    """The JSON content of the message"""

    summary: Optional[str] = None


class DataMessageChatContent(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    connection: Dict[str, object]
    """The channel data connection from the recipient to the underlying provider"""

    template: DataMessageChatContentTemplate

    metadata: Optional[Dict[str, object]] = None


class DataMessageInAppFeedContentBlockMessageInAppFeedContentBlock(BaseModel):
    content: str

    name: str

    rendered: str

    type: Literal["markdown", "text"]


class DataMessageInAppFeedContentBlockMessageInAppFeedButtonSetBlockButton(BaseModel):
    action: str

    label: str

    name: str


class DataMessageInAppFeedContentBlockMessageInAppFeedButtonSetBlock(BaseModel):
    buttons: List[DataMessageInAppFeedContentBlockMessageInAppFeedButtonSetBlockButton]

    name: str

    type: Literal["button_set"]


DataMessageInAppFeedContentBlock: TypeAlias = Union[
    DataMessageInAppFeedContentBlockMessageInAppFeedContentBlock,
    DataMessageInAppFeedContentBlockMessageInAppFeedButtonSetBlock,
]


class DataMessageInAppFeedContent(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    blocks: List[DataMessageInAppFeedContentBlock]
    """The blocks of the message"""


Data: TypeAlias = Union[
    DataMessageEmailContent,
    DataMessageSMSContent,
    DataMessagePushContent,
    DataMessageChatContent,
    DataMessageInAppFeedContent,
]


class MessageGetContentResponse(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    data: Data
    """The contents of an email message"""

    inserted_at: datetime

    message_id: str
