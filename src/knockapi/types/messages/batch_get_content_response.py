# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..message_contents import MessageContents

__all__ = ["BatchGetContentResponse"]

BatchGetContentResponse: TypeAlias = List[MessageContents]
