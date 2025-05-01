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
from ...types.integrations import census_custom_destination_params
from ...types.integrations.census_custom_destination_response import CensusCustomDestinationResponse

__all__ = ["CensusResource", "AsyncCensusResource"]


class CensusResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CensusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return CensusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CensusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return CensusResourceWithStreamingResponse(self)

    def custom_destination(
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
    ) -> CensusCustomDestinationResponse:
        """
        Processes a Census custom destination RPC request.

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
            "/v1/integrations/census/custom-destination",
            body=maybe_transform(
                {
                    "id": id,
                    "jsonrpc": jsonrpc,
                    "method": method,
                    "params": params,
                },
                census_custom_destination_params.CensusCustomDestinationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CensusCustomDestinationResponse,
        )


class AsyncCensusResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCensusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCensusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCensusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncCensusResourceWithStreamingResponse(self)

    async def custom_destination(
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
    ) -> CensusCustomDestinationResponse:
        """
        Processes a Census custom destination RPC request.

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
            "/v1/integrations/census/custom-destination",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "jsonrpc": jsonrpc,
                    "method": method,
                    "params": params,
                },
                census_custom_destination_params.CensusCustomDestinationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CensusCustomDestinationResponse,
        )


class CensusResourceWithRawResponse:
    def __init__(self, census: CensusResource) -> None:
        self._census = census

        self.custom_destination = to_raw_response_wrapper(
            census.custom_destination,
        )


class AsyncCensusResourceWithRawResponse:
    def __init__(self, census: AsyncCensusResource) -> None:
        self._census = census

        self.custom_destination = async_to_raw_response_wrapper(
            census.custom_destination,
        )


class CensusResourceWithStreamingResponse:
    def __init__(self, census: CensusResource) -> None:
        self._census = census

        self.custom_destination = to_streamed_response_wrapper(
            census.custom_destination,
        )


class AsyncCensusResourceWithStreamingResponse:
    def __init__(self, census: AsyncCensusResource) -> None:
        self._census = census

        self.custom_destination = async_to_streamed_response_wrapper(
            census.custom_destination,
        )
