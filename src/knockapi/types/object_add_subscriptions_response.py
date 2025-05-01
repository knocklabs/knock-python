# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .recipients.subscription import Subscription

__all__ = ["ObjectAddSubscriptionsResponse"]

ObjectAddSubscriptionsResponse: TypeAlias = List[Subscription]
