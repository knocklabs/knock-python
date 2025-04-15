# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
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
    "DataMessageInAppFeedContentBlockContentBlock",
    "DataMessageInAppFeedContentBlockButtonSetBlock",
    "DataMessageInAppFeedContentBlockButtonSetBlockButton",
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

    data: Optional[object] = None


class DataMessageChatContentTemplateBlock(BaseModel):
    content: str

    name: str

    type: Literal["text", "markdown"]


class DataMessageChatContentTemplate(BaseModel):
    blocks: Optional[List[DataMessageChatContentTemplateBlock]] = None
    """The structured blocks of the message"""

    json_content: Optional[object] = None
    """The JSON content of the message"""

    summary: Optional[str] = None


class DataMessageChatContent(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    connection: object
    """The channel data connection from the recipient to the underlying provider"""

    template: DataMessageChatContentTemplate

    metadata: Optional[object] = None


class DataMessageInAppFeedContentBlockContentBlock(BaseModel):
    content: str

    name: str

    rendered: str

    type: Literal["markdown", "text"]


class DataMessageInAppFeedContentBlockButtonSetBlockButton(BaseModel):
    action: str

    label: str

    name: str


class DataMessageInAppFeedContentBlockButtonSetBlock(BaseModel):
    buttons: List[DataMessageInAppFeedContentBlockButtonSetBlockButton]

    name: str

    type: Literal["button_set"]


DataMessageInAppFeedContentBlock: TypeAlias = Union[
    DataMessageInAppFeedContentBlockContentBlock, DataMessageInAppFeedContentBlockButtonSetBlock
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
