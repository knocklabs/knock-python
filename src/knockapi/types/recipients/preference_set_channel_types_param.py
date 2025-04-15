# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from ..shared_params.condition import Condition

__all__ = [
    "PreferenceSetChannelTypesParam",
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


class ChatConditions(TypedDict, total=False):
    conditions: Required[Iterable[Condition]]


Chat: TypeAlias = Union[bool, ChatConditions]


class EmailConditions(TypedDict, total=False):
    conditions: Required[Iterable[Condition]]


Email: TypeAlias = Union[bool, EmailConditions]


class HTTPConditions(TypedDict, total=False):
    conditions: Required[Iterable[Condition]]


HTTP: TypeAlias = Union[bool, HTTPConditions]


class InAppFeedConditions(TypedDict, total=False):
    conditions: Required[Iterable[Condition]]


InAppFeed: TypeAlias = Union[bool, InAppFeedConditions]


class PushConditions(TypedDict, total=False):
    conditions: Required[Iterable[Condition]]


Push: TypeAlias = Union[bool, PushConditions]


class SMSConditions(TypedDict, total=False):
    conditions: Required[Iterable[Condition]]


SMS: TypeAlias = Union[bool, SMSConditions]


class PreferenceSetChannelTypesParam(TypedDict, total=False):
    chat: Chat

    email: Email

    http: HTTP

    in_app_feed: InAppFeed

    push: Push

    sms: SMS
