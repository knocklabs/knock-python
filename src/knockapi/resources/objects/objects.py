# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

import httpx

from .bulk import (
    BulkResource,
    AsyncBulkResource,
    BulkResourceWithRawResponse,
    AsyncBulkResourceWithRawResponse,
    BulkResourceWithStreamingResponse,
    AsyncBulkResourceWithStreamingResponse,
)
from ...types import (
    object_list_params,
    object_set_channel_data_params,
    object_add_subscriptions_params,
    object_list_subscriptions_params,
    object_delete_subscriptions_params,
)
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
from ...pagination import SyncEntriesCursor, AsyncEntriesCursor
from ..._base_client import AsyncPaginator, make_request_options
from ...types.object import Object
from ...types.recipient_request_param import RecipientRequestParam
from ...types.recipients.channel_data import ChannelData
from ...types.recipients.subscription import Subscription
from ...types.recipient_reference_param import RecipientReferenceParam
from ...types.object_list_preferences_response import ObjectListPreferencesResponse
from ...types.object_add_subscriptions_response import ObjectAddSubscriptionsResponse
from ...types.object_delete_subscriptions_response import ObjectDeleteSubscriptionsResponse

__all__ = ["ObjectsResource", "AsyncObjectsResource"]


class ObjectsResource(SyncAPIResource):
    @cached_property
    def bulk(self) -> BulkResource:
        return BulkResource(self._client)

    @cached_property
    def with_raw_response(self) -> ObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/knock-python#accessing-raw-response-data-eg-headers
        """
        return ObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/knock-python#with_streaming_response
        """
        return ObjectsResourceWithStreamingResponse(self)

    def list(
        self,
        collection: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        include: List[Literal["preferences"]] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncEntriesCursor[Object]:
        """Returns a paginated list of objects from the specified collection.

        Optionally
        includes preference data for the objects.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          include: Includes preferences of the objects in the response.

          page_size: The number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        return self._get_api_list(
            f"/v1/objects/{collection}",
            page=SyncEntriesCursor[Object],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "include": include,
                        "page_size": page_size,
                    },
                    object_list_params.ObjectListParams,
                ),
            ),
            model=Object,
        )

    def add_subscriptions(
        self,
        collection: str,
        object_id: str,
        *,
        recipients: List[RecipientRequestParam],
        properties: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectAddSubscriptionsResponse:
        """Add subscriptions for an object.

        If a subscription already exists, it will be
        updated. This endpoint also handles
        [inline identifications](/managing-recipients/identifying-recipients#inline-identifying-recipients)
        for the `recipient`.

        Args:
          recipients: The recipients of the subscription.

          properties: The custom properties associated with the recipients of the subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._post(
            f"/v1/objects/{collection}/{object_id}/subscriptions",
            body=maybe_transform(
                {
                    "recipients": recipients,
                    "properties": properties,
                },
                object_add_subscriptions_params.ObjectAddSubscriptionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectAddSubscriptionsResponse,
        )

    def delete_subscriptions(
        self,
        collection: str,
        object_id: str,
        *,
        recipients: List[RecipientReferenceParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectDeleteSubscriptionsResponse:
        """Delete subscriptions for the specified recipients from an object.

        Returns the
        list of deleted subscriptions.

        Args:
          recipients: The recipients of the subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._delete(
            f"/v1/objects/{collection}/{object_id}/subscriptions",
            body=maybe_transform(
                {"recipients": recipients}, object_delete_subscriptions_params.ObjectDeleteSubscriptionsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectDeleteSubscriptionsResponse,
        )

    def get_channel_data(
        self,
        collection: str,
        object_id: str,
        channel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelData:
        """
        Returns the channel data for the specified object and channel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get(
            f"/v1/objects/{collection}/{object_id}/channel_data/{channel_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelData,
        )

    def list_preferences(
        self,
        collection: str,
        object_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectListPreferencesResponse:
        """
        Returns a paginated list of preference sets for the specified object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get(
            f"/v1/objects/{collection}/{object_id}/preferences",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectListPreferencesResponse,
        )

    def list_subscriptions(
        self,
        collection: str,
        object_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        include: List[Literal["preferences"]] | NotGiven = NOT_GIVEN,
        mode: Literal["recipient", "object"] | NotGiven = NOT_GIVEN,
        objects: List[RecipientReferenceParam] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        recipients: List[RecipientReferenceParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncEntriesCursor[Subscription]:
        """List subscriptions for an object.

        Either list the recipients that subscribe to
        the provided object, or list the objects that the provided object is subscribed
        to. Determined by the `mode` query parameter.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          include: Additional fields to include in the response.

          mode: Mode of the request.

          objects: Objects to filter by (only used if mode is `recipient`).

          page_size: The number of items per page.

          recipients: Recipients to filter by (only used if mode is `object`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get_api_list(
            f"/v1/objects/{collection}/{object_id}/subscriptions",
            page=SyncEntriesCursor[Subscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "include": include,
                        "mode": mode,
                        "objects": objects,
                        "page_size": page_size,
                        "recipients": recipients,
                    },
                    object_list_subscriptions_params.ObjectListSubscriptionsParams,
                ),
            ),
            model=Subscription,
        )

    def set_channel_data(
        self,
        collection: str,
        object_id: str,
        channel_id: str,
        *,
        data: object_set_channel_data_params.Data,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelData:
        """
        Sets the channel data for the specified object and channel.

        Args:
          data: Channel data for a given channel type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._put(
            f"/v1/objects/{collection}/{object_id}/channel_data/{channel_id}",
            body=maybe_transform({"data": data}, object_set_channel_data_params.ObjectSetChannelDataParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelData,
        )

    def unset_channel_data(
        self,
        collection: str,
        object_id: str,
        channel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Unsets the channel data for the specified object and channel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._delete(
            f"/v1/objects/{collection}/{object_id}/channel_data/{channel_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncObjectsResource(AsyncAPIResource):
    @cached_property
    def bulk(self) -> AsyncBulkResource:
        return AsyncBulkResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/knock-python#with_streaming_response
        """
        return AsyncObjectsResourceWithStreamingResponse(self)

    def list(
        self,
        collection: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        include: List[Literal["preferences"]] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Object, AsyncEntriesCursor[Object]]:
        """Returns a paginated list of objects from the specified collection.

        Optionally
        includes preference data for the objects.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          include: Includes preferences of the objects in the response.

          page_size: The number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        return self._get_api_list(
            f"/v1/objects/{collection}",
            page=AsyncEntriesCursor[Object],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "include": include,
                        "page_size": page_size,
                    },
                    object_list_params.ObjectListParams,
                ),
            ),
            model=Object,
        )

    async def add_subscriptions(
        self,
        collection: str,
        object_id: str,
        *,
        recipients: List[RecipientRequestParam],
        properties: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectAddSubscriptionsResponse:
        """Add subscriptions for an object.

        If a subscription already exists, it will be
        updated. This endpoint also handles
        [inline identifications](/managing-recipients/identifying-recipients#inline-identifying-recipients)
        for the `recipient`.

        Args:
          recipients: The recipients of the subscription.

          properties: The custom properties associated with the recipients of the subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._post(
            f"/v1/objects/{collection}/{object_id}/subscriptions",
            body=await async_maybe_transform(
                {
                    "recipients": recipients,
                    "properties": properties,
                },
                object_add_subscriptions_params.ObjectAddSubscriptionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectAddSubscriptionsResponse,
        )

    async def delete_subscriptions(
        self,
        collection: str,
        object_id: str,
        *,
        recipients: List[RecipientReferenceParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectDeleteSubscriptionsResponse:
        """Delete subscriptions for the specified recipients from an object.

        Returns the
        list of deleted subscriptions.

        Args:
          recipients: The recipients of the subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._delete(
            f"/v1/objects/{collection}/{object_id}/subscriptions",
            body=await async_maybe_transform(
                {"recipients": recipients}, object_delete_subscriptions_params.ObjectDeleteSubscriptionsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectDeleteSubscriptionsResponse,
        )

    async def get_channel_data(
        self,
        collection: str,
        object_id: str,
        channel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelData:
        """
        Returns the channel data for the specified object and channel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._get(
            f"/v1/objects/{collection}/{object_id}/channel_data/{channel_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelData,
        )

    async def list_preferences(
        self,
        collection: str,
        object_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectListPreferencesResponse:
        """
        Returns a paginated list of preference sets for the specified object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._get(
            f"/v1/objects/{collection}/{object_id}/preferences",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectListPreferencesResponse,
        )

    def list_subscriptions(
        self,
        collection: str,
        object_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        include: List[Literal["preferences"]] | NotGiven = NOT_GIVEN,
        mode: Literal["recipient", "object"] | NotGiven = NOT_GIVEN,
        objects: List[RecipientReferenceParam] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        recipients: List[RecipientReferenceParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Subscription, AsyncEntriesCursor[Subscription]]:
        """List subscriptions for an object.

        Either list the recipients that subscribe to
        the provided object, or list the objects that the provided object is subscribed
        to. Determined by the `mode` query parameter.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          include: Additional fields to include in the response.

          mode: Mode of the request.

          objects: Objects to filter by (only used if mode is `recipient`).

          page_size: The number of items per page.

          recipients: Recipients to filter by (only used if mode is `object`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get_api_list(
            f"/v1/objects/{collection}/{object_id}/subscriptions",
            page=AsyncEntriesCursor[Subscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "include": include,
                        "mode": mode,
                        "objects": objects,
                        "page_size": page_size,
                        "recipients": recipients,
                    },
                    object_list_subscriptions_params.ObjectListSubscriptionsParams,
                ),
            ),
            model=Subscription,
        )

    async def set_channel_data(
        self,
        collection: str,
        object_id: str,
        channel_id: str,
        *,
        data: object_set_channel_data_params.Data,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelData:
        """
        Sets the channel data for the specified object and channel.

        Args:
          data: Channel data for a given channel type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._put(
            f"/v1/objects/{collection}/{object_id}/channel_data/{channel_id}",
            body=await async_maybe_transform({"data": data}, object_set_channel_data_params.ObjectSetChannelDataParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelData,
        )

    async def unset_channel_data(
        self,
        collection: str,
        object_id: str,
        channel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Unsets the channel data for the specified object and channel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._delete(
            f"/v1/objects/{collection}/{object_id}/channel_data/{channel_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class ObjectsResourceWithRawResponse:
    def __init__(self, objects: ObjectsResource) -> None:
        self._objects = objects

        self.list = to_raw_response_wrapper(
            objects.list,
        )
        self.add_subscriptions = to_raw_response_wrapper(
            objects.add_subscriptions,
        )
        self.delete_subscriptions = to_raw_response_wrapper(
            objects.delete_subscriptions,
        )
        self.get_channel_data = to_raw_response_wrapper(
            objects.get_channel_data,
        )
        self.list_preferences = to_raw_response_wrapper(
            objects.list_preferences,
        )
        self.list_subscriptions = to_raw_response_wrapper(
            objects.list_subscriptions,
        )
        self.set_channel_data = to_raw_response_wrapper(
            objects.set_channel_data,
        )
        self.unset_channel_data = to_raw_response_wrapper(
            objects.unset_channel_data,
        )

    @cached_property
    def bulk(self) -> BulkResourceWithRawResponse:
        return BulkResourceWithRawResponse(self._objects.bulk)


class AsyncObjectsResourceWithRawResponse:
    def __init__(self, objects: AsyncObjectsResource) -> None:
        self._objects = objects

        self.list = async_to_raw_response_wrapper(
            objects.list,
        )
        self.add_subscriptions = async_to_raw_response_wrapper(
            objects.add_subscriptions,
        )
        self.delete_subscriptions = async_to_raw_response_wrapper(
            objects.delete_subscriptions,
        )
        self.get_channel_data = async_to_raw_response_wrapper(
            objects.get_channel_data,
        )
        self.list_preferences = async_to_raw_response_wrapper(
            objects.list_preferences,
        )
        self.list_subscriptions = async_to_raw_response_wrapper(
            objects.list_subscriptions,
        )
        self.set_channel_data = async_to_raw_response_wrapper(
            objects.set_channel_data,
        )
        self.unset_channel_data = async_to_raw_response_wrapper(
            objects.unset_channel_data,
        )

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithRawResponse:
        return AsyncBulkResourceWithRawResponse(self._objects.bulk)


class ObjectsResourceWithStreamingResponse:
    def __init__(self, objects: ObjectsResource) -> None:
        self._objects = objects

        self.list = to_streamed_response_wrapper(
            objects.list,
        )
        self.add_subscriptions = to_streamed_response_wrapper(
            objects.add_subscriptions,
        )
        self.delete_subscriptions = to_streamed_response_wrapper(
            objects.delete_subscriptions,
        )
        self.get_channel_data = to_streamed_response_wrapper(
            objects.get_channel_data,
        )
        self.list_preferences = to_streamed_response_wrapper(
            objects.list_preferences,
        )
        self.list_subscriptions = to_streamed_response_wrapper(
            objects.list_subscriptions,
        )
        self.set_channel_data = to_streamed_response_wrapper(
            objects.set_channel_data,
        )
        self.unset_channel_data = to_streamed_response_wrapper(
            objects.unset_channel_data,
        )

    @cached_property
    def bulk(self) -> BulkResourceWithStreamingResponse:
        return BulkResourceWithStreamingResponse(self._objects.bulk)


class AsyncObjectsResourceWithStreamingResponse:
    def __init__(self, objects: AsyncObjectsResource) -> None:
        self._objects = objects

        self.list = async_to_streamed_response_wrapper(
            objects.list,
        )
        self.add_subscriptions = async_to_streamed_response_wrapper(
            objects.add_subscriptions,
        )
        self.delete_subscriptions = async_to_streamed_response_wrapper(
            objects.delete_subscriptions,
        )
        self.get_channel_data = async_to_streamed_response_wrapper(
            objects.get_channel_data,
        )
        self.list_preferences = async_to_streamed_response_wrapper(
            objects.list_preferences,
        )
        self.list_subscriptions = async_to_streamed_response_wrapper(
            objects.list_subscriptions,
        )
        self.set_channel_data = async_to_streamed_response_wrapper(
            objects.set_channel_data,
        )
        self.unset_channel_data = async_to_streamed_response_wrapper(
            objects.unset_channel_data,
        )

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithStreamingResponse:
        return AsyncBulkResourceWithStreamingResponse(self._objects.bulk)
