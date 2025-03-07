# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.users import bulk_delete_params, bulk_identify_params, bulk_set_preferences_params
from ..._base_client import make_request_options
from ...types.users.bulk_delete_response import BulkDeleteResponse
from ...types.users.bulk_identify_response import BulkIdentifyResponse
from ...types.users.bulk_set_preferences_response import BulkSetPreferencesResponse
from ...types.shared_params.preference_set_request import PreferenceSetRequest
from ...types.shared_params.inline_identify_user_request import InlineIdentifyUserRequest

__all__ = ["BulkResource", "AsyncBulkResource"]


class BulkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/knock-python#accessing-raw-response-data-eg-headers
        """
        return BulkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/knock-python#with_streaming_response
        """
        return BulkResourceWithStreamingResponse(self)

    def delete(
        self,
        *,
        query_user_ids: List[str],
        body_user_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkDeleteResponse:
        """
        Bulk delete users

        Args:
          query_user_ids: The IDs of the users to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/bulk/delete",
            body=maybe_transform({"body_user_ids": body_user_ids}, bulk_delete_params.BulkDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query_user_ids": query_user_ids}, bulk_delete_params.BulkDeleteParams),
            ),
            cast_to=BulkDeleteResponse,
        )

    def identify(
        self,
        *,
        users: Iterable[InlineIdentifyUserRequest],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkIdentifyResponse:
        """
        Bulk identifies users

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/bulk/identify",
            body=maybe_transform({"users": users}, bulk_identify_params.BulkIdentifyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkIdentifyResponse,
        )

    def set_preferences(
        self,
        *,
        preferences: PreferenceSetRequest,
        user_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkSetPreferencesResponse:
        """
        Bulk set preferences

        Args:
          preferences: Set preferences for a recipient

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/users/bulk/preferences",
            body=maybe_transform(
                {
                    "preferences": preferences,
                    "user_ids": user_ids,
                },
                bulk_set_preferences_params.BulkSetPreferencesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkSetPreferencesResponse,
        )


class AsyncBulkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBulkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/knock-python#with_streaming_response
        """
        return AsyncBulkResourceWithStreamingResponse(self)

    async def delete(
        self,
        *,
        query_user_ids: List[str],
        body_user_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkDeleteResponse:
        """
        Bulk delete users

        Args:
          query_user_ids: The IDs of the users to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/bulk/delete",
            body=await async_maybe_transform({"body_user_ids": body_user_ids}, bulk_delete_params.BulkDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"query_user_ids": query_user_ids}, bulk_delete_params.BulkDeleteParams
                ),
            ),
            cast_to=BulkDeleteResponse,
        )

    async def identify(
        self,
        *,
        users: Iterable[InlineIdentifyUserRequest],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkIdentifyResponse:
        """
        Bulk identifies users

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/bulk/identify",
            body=await async_maybe_transform({"users": users}, bulk_identify_params.BulkIdentifyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkIdentifyResponse,
        )

    async def set_preferences(
        self,
        *,
        preferences: PreferenceSetRequest,
        user_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkSetPreferencesResponse:
        """
        Bulk set preferences

        Args:
          preferences: Set preferences for a recipient

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/users/bulk/preferences",
            body=await async_maybe_transform(
                {
                    "preferences": preferences,
                    "user_ids": user_ids,
                },
                bulk_set_preferences_params.BulkSetPreferencesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkSetPreferencesResponse,
        )


class BulkResourceWithRawResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.delete = to_raw_response_wrapper(
            bulk.delete,
        )
        self.identify = to_raw_response_wrapper(
            bulk.identify,
        )
        self.set_preferences = to_raw_response_wrapper(
            bulk.set_preferences,
        )


class AsyncBulkResourceWithRawResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.delete = async_to_raw_response_wrapper(
            bulk.delete,
        )
        self.identify = async_to_raw_response_wrapper(
            bulk.identify,
        )
        self.set_preferences = async_to_raw_response_wrapper(
            bulk.set_preferences,
        )


class BulkResourceWithStreamingResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.delete = to_streamed_response_wrapper(
            bulk.delete,
        )
        self.identify = to_streamed_response_wrapper(
            bulk.identify,
        )
        self.set_preferences = to_streamed_response_wrapper(
            bulk.set_preferences,
        )


class AsyncBulkResourceWithStreamingResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.delete = async_to_streamed_response_wrapper(
            bulk.delete,
        )
        self.identify = async_to_streamed_response_wrapper(
            bulk.identify,
        )
        self.set_preferences = async_to_streamed_response_wrapper(
            bulk.set_preferences,
        )
