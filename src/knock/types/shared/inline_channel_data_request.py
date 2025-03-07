# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

from .channel_data_request import ChannelDataRequest

__all__ = ["InlineChannelDataRequest"]

InlineChannelDataRequest: TypeAlias = Dict[str, ChannelDataRequest]
