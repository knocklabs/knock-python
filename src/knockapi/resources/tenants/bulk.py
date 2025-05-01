# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

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
from ...types.tenants import bulk_set_params, bulk_delete_params
from ...types.bulk_operation import BulkOperation
from ...types.inline_tenant_request_param import InlineTenantRequestParam

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

    def delete(
        self,
        *,
        tenant_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkOperation:
        """Delete multiple tenants in a single operation.

        This operation cannot be undone.

        Args:
          tenant_ids: The IDs of the tenants to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tenants/bulk/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"tenant_ids": tenant_ids}, bulk_delete_params.BulkDeleteParams),
            ),
            cast_to=BulkOperation,
        )

    def set(
        self,
        *,
        tenants: List[InlineTenantRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkOperation:
        """
        Set or update up to 1,000 tenants in a single operation.

        Args:
          tenants: The tenants to be upserted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tenants/bulk/set",
            body=maybe_transform({"tenants": tenants}, bulk_set_params.BulkSetParams),
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

    async def delete(
        self,
        *,
        tenant_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkOperation:
        """Delete multiple tenants in a single operation.

        This operation cannot be undone.

        Args:
          tenant_ids: The IDs of the tenants to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tenants/bulk/delete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"tenant_ids": tenant_ids}, bulk_delete_params.BulkDeleteParams),
            ),
            cast_to=BulkOperation,
        )

    async def set(
        self,
        *,
        tenants: List[InlineTenantRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkOperation:
        """
        Set or update up to 1,000 tenants in a single operation.

        Args:
          tenants: The tenants to be upserted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tenants/bulk/set",
            body=await async_maybe_transform({"tenants": tenants}, bulk_set_params.BulkSetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkOperation,
        )


class BulkResourceWithRawResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.delete = to_raw_response_wrapper(
            bulk.delete,
        )
        self.set = to_raw_response_wrapper(
            bulk.set,
        )


class AsyncBulkResourceWithRawResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.delete = async_to_raw_response_wrapper(
            bulk.delete,
        )
        self.set = async_to_raw_response_wrapper(
            bulk.set,
        )


class BulkResourceWithStreamingResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.delete = to_streamed_response_wrapper(
            bulk.delete,
        )
        self.set = to_streamed_response_wrapper(
            bulk.set,
        )


class AsyncBulkResourceWithStreamingResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.delete = async_to_streamed_response_wrapper(
            bulk.delete,
        )
        self.set = async_to_streamed_response_wrapper(
            bulk.set,
        )
