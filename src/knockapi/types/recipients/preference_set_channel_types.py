# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..shared.condition import Condition

__all__ = [
    "PreferenceSetChannelTypes",
    "Chat",
    "ChatConditions",
    "Email",
    "EmailConditions",
    "HTTP",
    "HTTPConditions",
    "InAppFeed",
    "InAppFeedConditions",
    "Push",
    "PushConditions",
    "SMS",
    "SMSConditions",
]


class ChatConditions(BaseModel):
    conditions: List[Condition]


Chat: TypeAlias = Union[bool, ChatConditions]


class EmailConditions(BaseModel):
    conditions: List[Condition]


Email: TypeAlias = Union[bool, EmailConditions]


class HTTPConditions(BaseModel):
    conditions: List[Condition]


HTTP: TypeAlias = Union[bool, HTTPConditions]


class InAppFeedConditions(BaseModel):
    conditions: List[Condition]


InAppFeed: TypeAlias = Union[bool, InAppFeedConditions]


class PushConditions(BaseModel):
    conditions: List[Condition]


Push: TypeAlias = Union[bool, PushConditions]


class SMSConditions(BaseModel):
    conditions: List[Condition]


SMS: TypeAlias = Union[bool, SMSConditions]


class PreferenceSetChannelTypes(BaseModel):
    chat: Optional[Chat] = None

    email: Optional[Email] = None

    http: Optional[HTTP] = None

    in_app_feed: Optional[InAppFeed] = None

    push: Optional[Push] = None

    sms: Optional[SMS] = None
