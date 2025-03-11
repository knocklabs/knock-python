# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "BatchGetContentResponse",
    "BatchGetContentResponseItem",
    "BatchGetContentResponseItemData",
    "BatchGetContentResponseItemDataMessageEmailContent",
    "BatchGetContentResponseItemDataMessageSMSContent",
    "BatchGetContentResponseItemDataMessagePushContent",
    "BatchGetContentResponseItemDataMessageChatContent",
    "BatchGetContentResponseItemDataMessageChatContentTemplate",
    "BatchGetContentResponseItemDataMessageChatContentTemplateBlock",
    "BatchGetContentResponseItemDataMessageInAppFeedContent",
    "BatchGetContentResponseItemDataMessageInAppFeedContentBlock",
    "BatchGetContentResponseItemDataMessageInAppFeedContentBlockMessageInAppFeedContentBlock",
    "BatchGetContentResponseItemDataMessageInAppFeedContentBlockMessageInAppFeedButtonSetBlock",
    "BatchGetContentResponseItemDataMessageInAppFeedContentBlockMessageInAppFeedButtonSetBlockButton",
]


class BatchGetContentResponseItemDataMessageEmailContent(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    from_: str = FieldInfo(alias="from")

    html_body: str

    subject_line: str

    text_body: str

    to: str

    bcc: Optional[str] = None

    cc: Optional[str] = None

    reply_to: Optional[str] = None


class BatchGetContentResponseItemDataMessageSMSContent(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    body: str

    to: str


class BatchGetContentResponseItemDataMessagePushContent(BaseModel):
    token: str

    api_typename: str = FieldInfo(alias="__typename")

    body: str

    title: str

    data: Optional[Dict[str, object]] = None


class BatchGetContentResponseItemDataMessageChatContentTemplateBlock(BaseModel):
    content: str

    name: str

    type: Literal["text", "markdown"]


class BatchGetContentResponseItemDataMessageChatContentTemplate(BaseModel):
    blocks: Optional[List[BatchGetContentResponseItemDataMessageChatContentTemplateBlock]] = None
    """The structured blocks of the message"""

    json_content: Optional[Dict[str, object]] = None
    """The JSON content of the message"""

    summary: Optional[str] = None


class BatchGetContentResponseItemDataMessageChatContent(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    connection: Dict[str, object]
    """The channel data connection from the recipient to the underlying provider"""

    template: BatchGetContentResponseItemDataMessageChatContentTemplate

    metadata: Optional[Dict[str, object]] = None


class BatchGetContentResponseItemDataMessageInAppFeedContentBlockMessageInAppFeedContentBlock(BaseModel):
    content: str

    name: str

    rendered: str

    type: Literal["markdown", "text"]


class BatchGetContentResponseItemDataMessageInAppFeedContentBlockMessageInAppFeedButtonSetBlockButton(BaseModel):
    action: str

    label: str

    name: str


class BatchGetContentResponseItemDataMessageInAppFeedContentBlockMessageInAppFeedButtonSetBlock(BaseModel):
    buttons: List[BatchGetContentResponseItemDataMessageInAppFeedContentBlockMessageInAppFeedButtonSetBlockButton]

    name: str

    type: Literal["button_set"]


BatchGetContentResponseItemDataMessageInAppFeedContentBlock: TypeAlias = Union[
    BatchGetContentResponseItemDataMessageInAppFeedContentBlockMessageInAppFeedContentBlock,
    BatchGetContentResponseItemDataMessageInAppFeedContentBlockMessageInAppFeedButtonSetBlock,
]


class BatchGetContentResponseItemDataMessageInAppFeedContent(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    blocks: List[BatchGetContentResponseItemDataMessageInAppFeedContentBlock]
    """The blocks of the message"""


BatchGetContentResponseItemData: TypeAlias = Union[
    BatchGetContentResponseItemDataMessageEmailContent,
    BatchGetContentResponseItemDataMessageSMSContent,
    BatchGetContentResponseItemDataMessagePushContent,
    BatchGetContentResponseItemDataMessageChatContent,
    BatchGetContentResponseItemDataMessageInAppFeedContent,
]


class BatchGetContentResponseItem(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")

    data: BatchGetContentResponseItemData
    """The contents of an email message"""

    inserted_at: datetime

    message_id: str


BatchGetContentResponse: TypeAlias = List[BatchGetContentResponseItem]
