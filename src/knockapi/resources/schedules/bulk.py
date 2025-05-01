# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ...types.schedules import bulk_create_params
from ...types.bulk_operation import BulkOperation

__all__ = ["BulkResource", "AsyncBulkResource"]


class BulkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return BulkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return BulkResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        schedules: Iterable[bulk_create_params.Schedule],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkOperation:
        """Bulk creates up to 1,000 schedules at a time.

        This endpoint also handles
        [inline identifications](/managing-recipients/identifying-recipients#inline-identifying-recipients)
        for the `actor`, `recipient`, and `tenant` fields.

        Args:
          schedules: A list of schedules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/schedules/bulk/create",
            body=maybe_transform({"schedules": schedules}, bulk_create_params.BulkCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkOperation,
        )


class AsyncBulkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBulkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncBulkResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        schedules: Iterable[bulk_create_params.Schedule],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkOperation:
        """Bulk creates up to 1,000 schedules at a time.

        This endpoint also handles
        [inline identifications](/managing-recipients/identifying-recipients#inline-identifying-recipients)
        for the `actor`, `recipient`, and `tenant` fields.

        Args:
          schedules: A list of schedules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/schedules/bulk/create",
            body=await async_maybe_transform({"schedules": schedules}, bulk_create_params.BulkCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkOperation,
        )


class BulkResourceWithRawResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.create = to_raw_response_wrapper(
            bulk.create,
        )


class AsyncBulkResourceWithRawResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.create = async_to_raw_response_wrapper(
            bulk.create,
        )


class BulkResourceWithStreamingResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.create = to_streamed_response_wrapper(
            bulk.create,
        )


class AsyncBulkResourceWithStreamingResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.create = async_to_streamed_response_wrapper(
            bulk.create,
        )
