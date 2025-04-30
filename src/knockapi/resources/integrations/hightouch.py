# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.integrations import hightouch_embedded_destination_params
from ...types.integrations.hightouch_embedded_destination_response import HightouchEmbeddedDestinationResponse

__all__ = ["HightouchResource", "AsyncHightouchResource"]


class HightouchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HightouchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return HightouchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HightouchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return HightouchResourceWithStreamingResponse(self)

    def embedded_destination(
        self,
        *,
        id: str,
        jsonrpc: str,
        method: str,
        params: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HightouchEmbeddedDestinationResponse:
        """
        Processes a Hightouch embedded destination RPC request.

        Args:
          id: The unique identifier for the RPC request.

          jsonrpc: The JSON-RPC version.

          method: The method name to execute.

          params: The parameters for the method.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/integrations/hightouch/embedded-destination",
            body=maybe_transform(
                {
                    "id": id,
                    "jsonrpc": jsonrpc,
                    "method": method,
                    "params": params,
                },
                hightouch_embedded_destination_params.HightouchEmbeddedDestinationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HightouchEmbeddedDestinationResponse,
        )


class AsyncHightouchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHightouchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHightouchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHightouchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncHightouchResourceWithStreamingResponse(self)

    async def embedded_destination(
        self,
        *,
        id: str,
        jsonrpc: str,
        method: str,
        params: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HightouchEmbeddedDestinationResponse:
        """
        Processes a Hightouch embedded destination RPC request.

        Args:
          id: The unique identifier for the RPC request.

          jsonrpc: The JSON-RPC version.

          method: The method name to execute.

          params: The parameters for the method.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/integrations/hightouch/embedded-destination",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "jsonrpc": jsonrpc,
                    "method": method,
                    "params": params,
                },
                hightouch_embedded_destination_params.HightouchEmbeddedDestinationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HightouchEmbeddedDestinationResponse,
        )


class HightouchResourceWithRawResponse:
    def __init__(self, hightouch: HightouchResource) -> None:
        self._hightouch = hightouch

        self.embedded_destination = to_raw_response_wrapper(
            hightouch.embedded_destination,
        )


class AsyncHightouchResourceWithRawResponse:
    def __init__(self, hightouch: AsyncHightouchResource) -> None:
        self._hightouch = hightouch

        self.embedded_destination = async_to_raw_response_wrapper(
            hightouch.embedded_destination,
        )


class HightouchResourceWithStreamingResponse:
    def __init__(self, hightouch: HightouchResource) -> None:
        self._hightouch = hightouch

        self.embedded_destination = to_streamed_response_wrapper(
            hightouch.embedded_destination,
        )


class AsyncHightouchResourceWithStreamingResponse:
    def __init__(self, hightouch: AsyncHightouchResource) -> None:
        self._hightouch = hightouch

        self.embedded_destination = async_to_streamed_response_wrapper(
            hightouch.embedded_destination,
        )
