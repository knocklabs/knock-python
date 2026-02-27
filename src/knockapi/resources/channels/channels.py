# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .bulk import (
    BulkResource,
    AsyncBulkResource,
    BulkResourceWithRawResponse,
    AsyncBulkResourceWithRawResponse,
    BulkResourceWithStreamingResponse,
    AsyncBulkResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ChannelsResource", "AsyncChannelsResource"]


class ChannelsResource(SyncAPIResource):
    @cached_property
    def bulk(self) -> BulkResource:
        """
        A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
        """
        return BulkResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return ChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return ChannelsResourceWithStreamingResponse(self)


class AsyncChannelsResource(AsyncAPIResource):
    @cached_property
    def bulk(self) -> AsyncBulkResource:
        """
        A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
        """
        return AsyncBulkResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncChannelsResourceWithStreamingResponse(self)


class ChannelsResourceWithRawResponse:
    def __init__(self, channels: ChannelsResource) -> None:
        self._channels = channels

    @cached_property
    def bulk(self) -> BulkResourceWithRawResponse:
        """
        A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
        """
        return BulkResourceWithRawResponse(self._channels.bulk)


class AsyncChannelsResourceWithRawResponse:
    def __init__(self, channels: AsyncChannelsResource) -> None:
        self._channels = channels

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithRawResponse:
        """
        A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
        """
        return AsyncBulkResourceWithRawResponse(self._channels.bulk)


class ChannelsResourceWithStreamingResponse:
    def __init__(self, channels: ChannelsResource) -> None:
        self._channels = channels

    @cached_property
    def bulk(self) -> BulkResourceWithStreamingResponse:
        """
        A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
        """
        return BulkResourceWithStreamingResponse(self._channels.bulk)


class AsyncChannelsResourceWithStreamingResponse:
    def __init__(self, channels: AsyncChannelsResource) -> None:
        self._channels = channels

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithStreamingResponse:
        """
        A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
        """
        return AsyncBulkResourceWithStreamingResponse(self._channels.bulk)
