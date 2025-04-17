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
    """The typename of the schema."""

    from_: str = FieldInfo(alias="from")
    """The sender's email address."""

    html_body: str
    """The HTML body of the email message."""

    subject_line: str
    """The subject line of the email message."""

    text_body: str
    """The text body of the email message."""

    to: str
    """The recipient's email address."""

    bcc: Optional[str] = None
    """The BCC email addresses."""

    cc: Optional[str] = None
    """The CC email addresses."""

    reply_to: Optional[str] = None
    """The reply-to email address."""


class BatchGetContentResponseItemDataMessageSMSContent(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    body: str
    """The content body of the SMS message."""

    to: str
    """The phone number the SMS was sent to."""


class BatchGetContentResponseItemDataMessagePushContent(BaseModel):
    token: str
    """The device token to send the push notification to."""

    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    body: str
    """The content body of the push notification."""

    title: str
    """The title of the push notification."""

    data: Optional[Dict[str, object]] = None
    """Additional data payload for the push notification."""


class BatchGetContentResponseItemDataMessageChatContentTemplateBlock(BaseModel):
    content: str
    """The actual content of the block."""

    name: str
    """The name of the block for identification."""

    type: Literal["text", "markdown"]
    """The type of block in a message in a chat (text or markdown)."""


class BatchGetContentResponseItemDataMessageChatContentTemplate(BaseModel):
    blocks: Optional[List[BatchGetContentResponseItemDataMessageChatContentTemplateBlock]] = None
    """The blocks of the message in a chat."""

    json_content: Optional[Dict[str, object]] = None
    """The JSON content of the message."""

    summary: Optional[str] = None
    """The summary of the chat message."""


class BatchGetContentResponseItemDataMessageChatContent(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    connection: Dict[str, object]
    """The channel data connection from the recipient to the underlying provider."""

    template: BatchGetContentResponseItemDataMessageChatContentTemplate
    """The template structure for the chat message."""

    metadata: Optional[Dict[str, object]] = None
    """Additional metadata associated with the chat message."""


class BatchGetContentResponseItemDataMessageInAppFeedContentBlockMessageInAppFeedContentBlock(BaseModel):
    content: str
    """The content of the block in a message in an app feed."""

    name: str
    """The name of the block in a message in an app feed."""

    rendered: str
    """The rendered HTML version of the content."""

    type: Literal["markdown", "text"]
    """The type of block in a message in an app feed."""


class BatchGetContentResponseItemDataMessageInAppFeedContentBlockMessageInAppFeedButtonSetBlockButton(BaseModel):
    action: str
    """The action to take when the button is clicked."""

    label: str
    """The label of the button."""

    name: str
    """The name of the button."""


class BatchGetContentResponseItemDataMessageInAppFeedContentBlockMessageInAppFeedButtonSetBlock(BaseModel):
    buttons: List[BatchGetContentResponseItemDataMessageInAppFeedContentBlockMessageInAppFeedButtonSetBlockButton]
    """A list of buttons in an in app feed message."""

    name: str
    """The name of the button set in a message in an app feed."""

    type: Literal["button_set"]
    """The type of block in a message in an app feed."""


BatchGetContentResponseItemDataMessageInAppFeedContentBlock: TypeAlias = Union[
    BatchGetContentResponseItemDataMessageInAppFeedContentBlockMessageInAppFeedContentBlock,
    BatchGetContentResponseItemDataMessageInAppFeedContentBlockMessageInAppFeedButtonSetBlock,
]


class BatchGetContentResponseItemDataMessageInAppFeedContent(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    blocks: List[BatchGetContentResponseItemDataMessageInAppFeedContentBlock]
    """The blocks of the message in an app feed."""


BatchGetContentResponseItemData: TypeAlias = Union[
    BatchGetContentResponseItemDataMessageEmailContent,
    BatchGetContentResponseItemDataMessageSMSContent,
    BatchGetContentResponseItemDataMessagePushContent,
    BatchGetContentResponseItemDataMessageChatContent,
    BatchGetContentResponseItemDataMessageInAppFeedContent,
]


class BatchGetContentResponseItem(BaseModel):
    api_typename: str = FieldInfo(alias="__typename")
    """The typename of the schema."""

    data: BatchGetContentResponseItemData
    """Content data specific to the channel type."""

    inserted_at: datetime
    """Timestamp when the message content was created."""

    message_id: str
    """The unique identifier for the message content."""


BatchGetContentResponse: TypeAlias = List[BatchGetContentResponseItem]
