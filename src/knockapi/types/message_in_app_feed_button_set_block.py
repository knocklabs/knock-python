# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MessageInAppFeedButtonSetBlock", "Button"]


class Button(BaseModel):
    """A button in an in app feed message."""

    action: str
    """The action to take when the button is clicked."""

    label: str
    """The label of the button."""

    name: str
    """The name of the button."""


class MessageInAppFeedButtonSetBlock(BaseModel):
    """A button set block in a message in an app feed."""

    buttons: List[Button]
    """A list of buttons in an in app feed message."""

    name: str
    """The name of the button set in a message in an app feed."""

    type: Literal["button_set"]
    """The type of block in a message in an app feed."""
