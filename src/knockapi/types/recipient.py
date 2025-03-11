# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .user import User
from .object import Object

__all__ = ["Recipient"]

Recipient: TypeAlias = Union[User, Object]
