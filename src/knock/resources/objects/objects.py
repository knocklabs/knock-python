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
    object_set_params,
    object_list_params,
    object_list_messages_params,
    object_list_schedules_params,
    object_get_preferences_params,
    object_set_preferences_params,
    object_set_channel_data_params,
    object_add_subscriptions_params,
    object_list_subscriptions_params,
    object_delete_subscriptions_params,
)
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
from ...pagination import SyncEntriesCursor, AsyncEntriesCursor
from ..._base_client import AsyncPaginator, make_request_options
from ...types.message import Message
from ...types.shared.object import Object
from ...types.shared.schedule import Schedule
from ...types.shared.channel_data import ChannelData
from ...types.shared.subscription import Subscription
from ...types.shared.preference_set import PreferenceSet
from ...types.shared_params.recipient_request import RecipientRequest
from ...types.object_list_preferences_response import ObjectListPreferencesResponse
from ...types.object_add_subscriptions_response import ObjectAddSubscriptionsResponse
from ...types.object_delete_subscriptions_response import ObjectDeleteSubscriptionsResponse
from ...types.shared_params.inline_channel_data_request import InlineChannelDataRequest
from ...types.shared_params.preference_set_channel_types import PreferenceSetChannelTypes
from ...types.shared_params.inline_preference_set_request import InlinePreferenceSetRequest

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
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncEntriesCursor[Object]:
        """
        List objects in a collection

        Args:
          after: The cursor to fetch entries after

          before: The cursor to fetch entries before

          page_size: The page size to fetch

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
                        "page_size": page_size,
                    },
                    object_list_params.ObjectListParams,
                ),
            ),
            model=Object,
        )

    def delete(
        self,
        id: str,
        *,
        collection: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Delete an object

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/v1/objects/{collection}/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def add_subscriptions(
        self,
        object_id: str,
        *,
        collection: str,
        recipients: List[RecipientRequest],
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
        updated.

        Args:
          recipients: The recipients to subscribe to the object

          properties: The custom properties associated with the subscription

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
        object_id: str,
        *,
        collection: str,
        recipients: List[RecipientRequest],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectDeleteSubscriptionsResponse:
        """
        Delete subscriptions

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

    def get(
        self,
        id: str,
        *,
        collection: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Object:
        """
        Get an object

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/objects/{collection}/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Object,
        )

    def get_channel_data(
        self,
        channel_id: str,
        *,
        collection: str,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelData:
        """
        Get channel data

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

    def get_preferences(
        self,
        id: str,
        *,
        collection: str,
        object_id: str,
        tenant: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreferenceSet:
        """
        Get a preference set

        Args:
          tenant: Tenant ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/objects/{collection}/{object_id}/preferences/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"tenant": tenant}, object_get_preferences_params.ObjectGetPreferencesParams),
            ),
            cast_to=PreferenceSet,
        )

    def list_messages(
        self,
        id: str,
        *,
        collection: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        channel_id: str | NotGiven = NOT_GIVEN,
        engagement_status: List[Literal["seen", "read", "interacted", "link_clicked", "archived"]]
        | NotGiven = NOT_GIVEN,
        message_ids: List[str] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        source: str | NotGiven = NOT_GIVEN,
        status: List[Literal["queued", "sent", "delivered", "delivery_attempted", "undelivered", "not_sent", "bounced"]]
        | NotGiven = NOT_GIVEN,
        tenant: str | NotGiven = NOT_GIVEN,
        trigger_data: str | NotGiven = NOT_GIVEN,
        workflow_categories: List[str] | NotGiven = NOT_GIVEN,
        workflow_recipient_run_id: str | NotGiven = NOT_GIVEN,
        workflow_run_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncEntriesCursor[Message]:
        """
        List messages

        Args:
          after: The cursor to fetch entries after

          before: The cursor to fetch entries before

          channel_id: The channel ID

          engagement_status: The engagement status of the message

          message_ids: The message IDs to filter messages by

          page_size: The page size to fetch

          source: The source of the message (workflow key)

          status: The status of the message

          tenant: The tenant ID

          trigger_data: The trigger data to filter messages by. Must be a valid JSON object.

          workflow_categories: The workflow categories to filter messages by

          workflow_recipient_run_id: The workflow recipient run ID to filter messages by

          workflow_run_id: The workflow run ID to filter messages by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            f"/v1/objects/{collection}/{id}/messages",
            page=SyncEntriesCursor[Message],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "channel_id": channel_id,
                        "engagement_status": engagement_status,
                        "message_ids": message_ids,
                        "page_size": page_size,
                        "source": source,
                        "status": status,
                        "tenant": tenant,
                        "trigger_data": trigger_data,
                        "workflow_categories": workflow_categories,
                        "workflow_recipient_run_id": workflow_recipient_run_id,
                        "workflow_run_id": workflow_run_id,
                    },
                    object_list_messages_params.ObjectListMessagesParams,
                ),
            ),
            model=Message,
        )

    def list_preferences(
        self,
        object_id: str,
        *,
        collection: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectListPreferencesResponse:
        """
        List preference sets

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

    def list_schedules(
        self,
        id: str,
        *,
        collection: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        tenant: str | NotGiven = NOT_GIVEN,
        workflow: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncEntriesCursor[Schedule]:
        """
        List schedules

        Args:
          after: The cursor to fetch entries after

          before: The cursor to fetch entries before

          page_size: The page size to fetch

          tenant: The ID of the tenant to list schedules for

          workflow: The ID of the workflow to list schedules for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            f"/v1/objects/{collection}/{id}/schedules",
            page=SyncEntriesCursor[Schedule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "page_size": page_size,
                        "tenant": tenant,
                        "workflow": workflow,
                    },
                    object_list_schedules_params.ObjectListSchedulesParams,
                ),
            ),
            model=Schedule,
        )

    def list_subscriptions(
        self,
        object_id: str,
        *,
        collection: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        mode: Literal["recipient", "object"] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        recipients: List[object_list_subscriptions_params.Recipient] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncEntriesCursor[Subscription]:
        """List subscriptions for an object.

        Either list all subscriptions that belong to
        the object, or all subscriptions that this object has. Determined by the `mode`
        query parameter.

        Args:
          after: The cursor to fetch entries after

          before: The cursor to fetch entries before

          mode: Mode of the request

          page_size: The page size to fetch

          recipients: Recipients to filter by (only used if mode is `object`)

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
                        "mode": mode,
                        "page_size": page_size,
                        "recipients": recipients,
                    },
                    object_list_subscriptions_params.ObjectListSubscriptionsParams,
                ),
            ),
            model=Subscription,
        )

    def set(
        self,
        id: str,
        *,
        collection: str,
        channel_data: Optional[InlineChannelDataRequest] | NotGiven = NOT_GIVEN,
        preferences: Optional[InlinePreferenceSetRequest] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Object:
        """
        Set (identify) an object

        Args:
          channel_data: Allows inline setting channel data for a recipient

          preferences: Inline set preferences for a recipient, where the key is the preference set name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/v1/objects/{collection}/{id}",
            body=maybe_transform(
                {
                    "channel_data": channel_data,
                    "preferences": preferences,
                },
                object_set_params.ObjectSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Object,
        )

    def set_channel_data(
        self,
        channel_id: str,
        *,
        collection: str,
        object_id: str,
        data: object_set_channel_data_params.Data,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelData:
        """
        Set channel data

        Args:
          data: Channel data for push providers

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

    def set_preferences(
        self,
        id: str,
        *,
        collection: str,
        object_id: str,
        categories: Optional[Dict[str, object_set_preferences_params.Categories]] | NotGiven = NOT_GIVEN,
        channel_types: Optional[PreferenceSetChannelTypes] | NotGiven = NOT_GIVEN,
        workflows: Optional[Dict[str, object_set_preferences_params.Workflows]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreferenceSet:
        """
        Update a preference set

        Args:
          categories: A setting for a preference set, where the key in the object is the category, and
              the values are the preference settings for that category.

          channel_types: Channel type preferences

          workflows: A setting for a preference set, where the key in the object is the workflow key,
              and the values are the preference settings for that workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/v1/objects/{collection}/{object_id}/preferences/{id}",
            body=maybe_transform(
                {
                    "categories": categories,
                    "channel_types": channel_types,
                    "workflows": workflows,
                },
                object_set_preferences_params.ObjectSetPreferencesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceSet,
        )

    def unset_channel_data(
        self,
        channel_id: str,
        *,
        collection: str,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Unset channel data

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
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Object, AsyncEntriesCursor[Object]]:
        """
        List objects in a collection

        Args:
          after: The cursor to fetch entries after

          before: The cursor to fetch entries before

          page_size: The page size to fetch

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
                        "page_size": page_size,
                    },
                    object_list_params.ObjectListParams,
                ),
            ),
            model=Object,
        )

    async def delete(
        self,
        id: str,
        *,
        collection: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Delete an object

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/v1/objects/{collection}/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def add_subscriptions(
        self,
        object_id: str,
        *,
        collection: str,
        recipients: List[RecipientRequest],
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
        updated.

        Args:
          recipients: The recipients to subscribe to the object

          properties: The custom properties associated with the subscription

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
        object_id: str,
        *,
        collection: str,
        recipients: List[RecipientRequest],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectDeleteSubscriptionsResponse:
        """
        Delete subscriptions

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

    async def get(
        self,
        id: str,
        *,
        collection: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Object:
        """
        Get an object

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/objects/{collection}/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Object,
        )

    async def get_channel_data(
        self,
        channel_id: str,
        *,
        collection: str,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelData:
        """
        Get channel data

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

    async def get_preferences(
        self,
        id: str,
        *,
        collection: str,
        object_id: str,
        tenant: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreferenceSet:
        """
        Get a preference set

        Args:
          tenant: Tenant ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/objects/{collection}/{object_id}/preferences/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"tenant": tenant}, object_get_preferences_params.ObjectGetPreferencesParams
                ),
            ),
            cast_to=PreferenceSet,
        )

    def list_messages(
        self,
        id: str,
        *,
        collection: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        channel_id: str | NotGiven = NOT_GIVEN,
        engagement_status: List[Literal["seen", "read", "interacted", "link_clicked", "archived"]]
        | NotGiven = NOT_GIVEN,
        message_ids: List[str] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        source: str | NotGiven = NOT_GIVEN,
        status: List[Literal["queued", "sent", "delivered", "delivery_attempted", "undelivered", "not_sent", "bounced"]]
        | NotGiven = NOT_GIVEN,
        tenant: str | NotGiven = NOT_GIVEN,
        trigger_data: str | NotGiven = NOT_GIVEN,
        workflow_categories: List[str] | NotGiven = NOT_GIVEN,
        workflow_recipient_run_id: str | NotGiven = NOT_GIVEN,
        workflow_run_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Message, AsyncEntriesCursor[Message]]:
        """
        List messages

        Args:
          after: The cursor to fetch entries after

          before: The cursor to fetch entries before

          channel_id: The channel ID

          engagement_status: The engagement status of the message

          message_ids: The message IDs to filter messages by

          page_size: The page size to fetch

          source: The source of the message (workflow key)

          status: The status of the message

          tenant: The tenant ID

          trigger_data: The trigger data to filter messages by. Must be a valid JSON object.

          workflow_categories: The workflow categories to filter messages by

          workflow_recipient_run_id: The workflow recipient run ID to filter messages by

          workflow_run_id: The workflow run ID to filter messages by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            f"/v1/objects/{collection}/{id}/messages",
            page=AsyncEntriesCursor[Message],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "channel_id": channel_id,
                        "engagement_status": engagement_status,
                        "message_ids": message_ids,
                        "page_size": page_size,
                        "source": source,
                        "status": status,
                        "tenant": tenant,
                        "trigger_data": trigger_data,
                        "workflow_categories": workflow_categories,
                        "workflow_recipient_run_id": workflow_recipient_run_id,
                        "workflow_run_id": workflow_run_id,
                    },
                    object_list_messages_params.ObjectListMessagesParams,
                ),
            ),
            model=Message,
        )

    async def list_preferences(
        self,
        object_id: str,
        *,
        collection: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectListPreferencesResponse:
        """
        List preference sets

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

    def list_schedules(
        self,
        id: str,
        *,
        collection: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        tenant: str | NotGiven = NOT_GIVEN,
        workflow: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Schedule, AsyncEntriesCursor[Schedule]]:
        """
        List schedules

        Args:
          after: The cursor to fetch entries after

          before: The cursor to fetch entries before

          page_size: The page size to fetch

          tenant: The ID of the tenant to list schedules for

          workflow: The ID of the workflow to list schedules for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            f"/v1/objects/{collection}/{id}/schedules",
            page=AsyncEntriesCursor[Schedule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "page_size": page_size,
                        "tenant": tenant,
                        "workflow": workflow,
                    },
                    object_list_schedules_params.ObjectListSchedulesParams,
                ),
            ),
            model=Schedule,
        )

    def list_subscriptions(
        self,
        object_id: str,
        *,
        collection: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        mode: Literal["recipient", "object"] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        recipients: List[object_list_subscriptions_params.Recipient] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Subscription, AsyncEntriesCursor[Subscription]]:
        """List subscriptions for an object.

        Either list all subscriptions that belong to
        the object, or all subscriptions that this object has. Determined by the `mode`
        query parameter.

        Args:
          after: The cursor to fetch entries after

          before: The cursor to fetch entries before

          mode: Mode of the request

          page_size: The page size to fetch

          recipients: Recipients to filter by (only used if mode is `object`)

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
                        "mode": mode,
                        "page_size": page_size,
                        "recipients": recipients,
                    },
                    object_list_subscriptions_params.ObjectListSubscriptionsParams,
                ),
            ),
            model=Subscription,
        )

    async def set(
        self,
        id: str,
        *,
        collection: str,
        channel_data: Optional[InlineChannelDataRequest] | NotGiven = NOT_GIVEN,
        preferences: Optional[InlinePreferenceSetRequest] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Object:
        """
        Set (identify) an object

        Args:
          channel_data: Allows inline setting channel data for a recipient

          preferences: Inline set preferences for a recipient, where the key is the preference set name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/v1/objects/{collection}/{id}",
            body=await async_maybe_transform(
                {
                    "channel_data": channel_data,
                    "preferences": preferences,
                },
                object_set_params.ObjectSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Object,
        )

    async def set_channel_data(
        self,
        channel_id: str,
        *,
        collection: str,
        object_id: str,
        data: object_set_channel_data_params.Data,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChannelData:
        """
        Set channel data

        Args:
          data: Channel data for push providers

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

    async def set_preferences(
        self,
        id: str,
        *,
        collection: str,
        object_id: str,
        categories: Optional[Dict[str, object_set_preferences_params.Categories]] | NotGiven = NOT_GIVEN,
        channel_types: Optional[PreferenceSetChannelTypes] | NotGiven = NOT_GIVEN,
        workflows: Optional[Dict[str, object_set_preferences_params.Workflows]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreferenceSet:
        """
        Update a preference set

        Args:
          categories: A setting for a preference set, where the key in the object is the category, and
              the values are the preference settings for that category.

          channel_types: Channel type preferences

          workflows: A setting for a preference set, where the key in the object is the workflow key,
              and the values are the preference settings for that workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/v1/objects/{collection}/{object_id}/preferences/{id}",
            body=await async_maybe_transform(
                {
                    "categories": categories,
                    "channel_types": channel_types,
                    "workflows": workflows,
                },
                object_set_preferences_params.ObjectSetPreferencesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceSet,
        )

    async def unset_channel_data(
        self,
        channel_id: str,
        *,
        collection: str,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Unset channel data

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
        self.delete = to_raw_response_wrapper(
            objects.delete,
        )
        self.add_subscriptions = to_raw_response_wrapper(
            objects.add_subscriptions,
        )
        self.delete_subscriptions = to_raw_response_wrapper(
            objects.delete_subscriptions,
        )
        self.get = to_raw_response_wrapper(
            objects.get,
        )
        self.get_channel_data = to_raw_response_wrapper(
            objects.get_channel_data,
        )
        self.get_preferences = to_raw_response_wrapper(
            objects.get_preferences,
        )
        self.list_messages = to_raw_response_wrapper(
            objects.list_messages,
        )
        self.list_preferences = to_raw_response_wrapper(
            objects.list_preferences,
        )
        self.list_schedules = to_raw_response_wrapper(
            objects.list_schedules,
        )
        self.list_subscriptions = to_raw_response_wrapper(
            objects.list_subscriptions,
        )
        self.set = to_raw_response_wrapper(
            objects.set,
        )
        self.set_channel_data = to_raw_response_wrapper(
            objects.set_channel_data,
        )
        self.set_preferences = to_raw_response_wrapper(
            objects.set_preferences,
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
        self.delete = async_to_raw_response_wrapper(
            objects.delete,
        )
        self.add_subscriptions = async_to_raw_response_wrapper(
            objects.add_subscriptions,
        )
        self.delete_subscriptions = async_to_raw_response_wrapper(
            objects.delete_subscriptions,
        )
        self.get = async_to_raw_response_wrapper(
            objects.get,
        )
        self.get_channel_data = async_to_raw_response_wrapper(
            objects.get_channel_data,
        )
        self.get_preferences = async_to_raw_response_wrapper(
            objects.get_preferences,
        )
        self.list_messages = async_to_raw_response_wrapper(
            objects.list_messages,
        )
        self.list_preferences = async_to_raw_response_wrapper(
            objects.list_preferences,
        )
        self.list_schedules = async_to_raw_response_wrapper(
            objects.list_schedules,
        )
        self.list_subscriptions = async_to_raw_response_wrapper(
            objects.list_subscriptions,
        )
        self.set = async_to_raw_response_wrapper(
            objects.set,
        )
        self.set_channel_data = async_to_raw_response_wrapper(
            objects.set_channel_data,
        )
        self.set_preferences = async_to_raw_response_wrapper(
            objects.set_preferences,
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
        self.delete = to_streamed_response_wrapper(
            objects.delete,
        )
        self.add_subscriptions = to_streamed_response_wrapper(
            objects.add_subscriptions,
        )
        self.delete_subscriptions = to_streamed_response_wrapper(
            objects.delete_subscriptions,
        )
        self.get = to_streamed_response_wrapper(
            objects.get,
        )
        self.get_channel_data = to_streamed_response_wrapper(
            objects.get_channel_data,
        )
        self.get_preferences = to_streamed_response_wrapper(
            objects.get_preferences,
        )
        self.list_messages = to_streamed_response_wrapper(
            objects.list_messages,
        )
        self.list_preferences = to_streamed_response_wrapper(
            objects.list_preferences,
        )
        self.list_schedules = to_streamed_response_wrapper(
            objects.list_schedules,
        )
        self.list_subscriptions = to_streamed_response_wrapper(
            objects.list_subscriptions,
        )
        self.set = to_streamed_response_wrapper(
            objects.set,
        )
        self.set_channel_data = to_streamed_response_wrapper(
            objects.set_channel_data,
        )
        self.set_preferences = to_streamed_response_wrapper(
            objects.set_preferences,
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
        self.delete = async_to_streamed_response_wrapper(
            objects.delete,
        )
        self.add_subscriptions = async_to_streamed_response_wrapper(
            objects.add_subscriptions,
        )
        self.delete_subscriptions = async_to_streamed_response_wrapper(
            objects.delete_subscriptions,
        )
        self.get = async_to_streamed_response_wrapper(
            objects.get,
        )
        self.get_channel_data = async_to_streamed_response_wrapper(
            objects.get_channel_data,
        )
        self.get_preferences = async_to_streamed_response_wrapper(
            objects.get_preferences,
        )
        self.list_messages = async_to_streamed_response_wrapper(
            objects.list_messages,
        )
        self.list_preferences = async_to_streamed_response_wrapper(
            objects.list_preferences,
        )
        self.list_schedules = async_to_streamed_response_wrapper(
            objects.list_schedules,
        )
        self.list_subscriptions = async_to_streamed_response_wrapper(
            objects.list_subscriptions,
        )
        self.set = async_to_streamed_response_wrapper(
            objects.set,
        )
        self.set_channel_data = async_to_streamed_response_wrapper(
            objects.set_channel_data,
        )
        self.set_preferences = async_to_streamed_response_wrapper(
            objects.set_preferences,
        )
        self.unset_channel_data = async_to_streamed_response_wrapper(
            objects.unset_channel_data,
        )

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithStreamingResponse:
        return AsyncBulkResourceWithStreamingResponse(self._objects.bulk)
