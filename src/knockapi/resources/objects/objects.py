# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
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
    object_set_preferences_params,
    object_set_channel_data_params,
    object_add_subscriptions_params,
    object_list_subscriptions_params,
    object_delete_subscriptions_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncItemsCursor, AsyncItemsCursor, SyncEntriesCursor, AsyncEntriesCursor
from ..._base_client import AsyncPaginator, make_request_options
from ...types.object import Object
from ...types.message import Message
from ...types.schedule import Schedule
from ...types.recipient_request_param import RecipientRequestParam
from ...types.recipients.channel_data import ChannelData
from ...types.recipients.subscription import Subscription
from ...types.recipient_reference_param import RecipientReferenceParam
from ...types.recipients.preference_set import PreferenceSet
from ...types.object_list_preferences_response import ObjectListPreferencesResponse
from ...types.object_add_subscriptions_response import ObjectAddSubscriptionsResponse
from ...types.object_delete_subscriptions_response import ObjectDeleteSubscriptionsResponse
from ...types.recipients.inline_channel_data_request_param import InlineChannelDataRequestParam
from ...types.recipients.preference_set_channel_types_param import PreferenceSetChannelTypesParam
from ...types.recipients.inline_preference_set_request_param import InlinePreferenceSetRequestParam

__all__ = ["ObjectsResource", "AsyncObjectsResource"]


class ObjectsResource(SyncAPIResource):
    """An object represents a resource in your system that you want to map into Knock."""

    @cached_property
    def bulk(self) -> BulkResource:
        """
        A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
        """
        return BulkResource(self._client)

    @cached_property
    def with_raw_response(self) -> ObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return ObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return ObjectsResourceWithStreamingResponse(self)

    def list(
        self,
        collection: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        include: List[Literal["preferences"]] | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEntriesCursor[Object]:
        """Returns a paginated list of objects from the specified collection.

        Optionally
        includes preference data for the objects.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          include: Includes preferences of the objects in the response.

          page_size: The number of items per page (defaults to 50).

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

    def delete(
        self,
        collection: str,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Permanently removes an object from the specified collection.

        This operation
        cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/objects/{collection}/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def add_subscriptions(
        self,
        collection: str,
        object_id: str,
        *,
        recipients: SequenceNotStr[RecipientRequestParam],
        properties: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ObjectAddSubscriptionsResponse:
        """Add subscriptions for an object.

        If a subscription already exists, it will be
        updated. This endpoint also handles
        [inline identifications](/managing-recipients/identifying-recipients#inline-identifying-recipients)
        for the `recipient`.

        Args:
          recipients: The recipients of the subscription. You can subscribe up to 100 recipients to an
              object at a time.

          properties: The custom properties associated with the subscription relationship.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ObjectAddSubscriptionsResponse,
        )

    def delete_subscriptions(
        self,
        collection: str,
        object_id: str,
        *,
        recipients: SequenceNotStr[RecipientReferenceParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ObjectDeleteSubscriptionsResponse:
        """Delete subscriptions for the specified recipients from an object.

        Returns the
        list of deleted subscriptions.

        Args:
          recipients: The recipients of the subscription. You can subscribe up to 100 recipients to an
              object at a time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ObjectDeleteSubscriptionsResponse,
        )

    def get(
        self,
        collection: str,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Object:
        """Retrieves a specific object by its ID from the specified collection.

        Returns the
        object with all its properties.

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
        collection: str,
        object_id: str,
        channel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    def get_preferences(
        self,
        collection: str,
        object_id: str,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceSet:
        """
        Returns the preference set for the specified object and preference set `id`.

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/objects/{collection}/{object_id}/preferences/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceSet,
        )

    def list_messages(
        self,
        collection: str,
        id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        channel_id: str | Omit = omit,
        engagement_status: List[
            Literal["seen", "unseen", "read", "unread", "archived", "unarchived", "link_clicked", "interacted"]
        ]
        | Omit = omit,
        inserted_at: object_list_messages_params.InsertedAt | Omit = omit,
        message_ids: SequenceNotStr[str] | Omit = omit,
        page_size: int | Omit = omit,
        source: str | Omit = omit,
        status: List[Literal["queued", "sent", "delivered", "delivery_attempted", "undelivered", "not_sent", "bounced"]]
        | Omit = omit,
        tenant: str | Omit = omit,
        trigger_data: str | Omit = omit,
        workflow_categories: SequenceNotStr[str] | Omit = omit,
        workflow_recipient_run_id: str | Omit = omit,
        workflow_run_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncItemsCursor[Message]:
        """
        Returns a paginated list of messages for a specific object in the given
        collection. Allows filtering by message status and provides various sorting
        options.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          channel_id: Limits the results to items with the corresponding channel ID.

          engagement_status: Limits the results to messages with the given engagement status.

          message_ids: Limits the results to only the message IDs given (max 50). Note: when using this
              option, the results will be subject to any other filters applied to the query.

          page_size: The number of items per page (defaults to 50).

          source: Limits the results to messages triggered by the given workflow key.

          status: Limits the results to messages with the given delivery status.

          tenant: Limits the results to items with the corresponding tenant.

          trigger_data: Limits the results to only messages that were generated with the given data. See
              [trigger data filtering](/api-reference/overview/trigger-data-filtering) for
              more information.

          workflow_categories: Limits the results to messages related to any of the provided categories.

          workflow_recipient_run_id: Limits the results to messages for a specific recipient's workflow run.

          workflow_run_id: Limits the results to messages associated with the top-level workflow run ID
              returned by the workflow trigger request.

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
            page=SyncItemsCursor[Message],
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
                        "inserted_at": inserted_at,
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
        collection: str,
        object_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    def list_schedules(
        self,
        collection: str,
        id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        page_size: int | Omit = omit,
        tenant: str | Omit = omit,
        workflow: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEntriesCursor[Schedule]:
        """
        Returns a paginated list of schedules for an object.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          page_size: The number of items per page (defaults to 50).

          tenant: Filter schedules by tenant id.

          workflow: Filter schedules by workflow id.

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
        collection: str,
        object_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        include: List[Literal["preferences"]] | Omit = omit,
        mode: Literal["recipient", "object"] | Omit = omit,
        objects: Iterable[object_list_subscriptions_params.Object] | Omit = omit,
        page_size: int | Omit = omit,
        recipients: SequenceNotStr[RecipientReferenceParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEntriesCursor[Subscription]:
        """List subscriptions for an object.

        Either list the recipients that subscribe to
        the provided object, or list the objects that the provided object is subscribed
        to. Determined by the `mode` query parameter.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          include: Additional fields to include in the response.

          mode: Mode of the request. `recipient` to list the objects that the provided object is
              subscribed to, `object` to list the recipients that subscribe to the provided
              object.

          objects: Objects to filter by (only used if mode is `recipient`).

          page_size: The number of items per page (defaults to 50).

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

    def set(
        self,
        collection: str,
        id: str,
        *,
        channel_data: InlineChannelDataRequestParam | Omit = omit,
        locale: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        preferences: InlinePreferenceSetRequestParam | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Object:
        """
        Creates a new object or updates an existing one in the specified collection.
        This operation is used to identify objects with their properties, as well as
        optional preferences and channel data.

        Args:
          channel_data: A request to set channel data for a type of channel inline.

          locale: The locale of the object. Used for
              [message localization](/concepts/translations).

          name: An optional name for the object.

          preferences: Inline set preferences for a recipient, where the key is the preference set id.
              Preferences that are set inline will be merged into any existing preferences
              rather than replacing them.

          timezone: The timezone of the object. Must be a
              valid [tz database time zone string](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
              Used
              for [recurring schedules](/concepts/schedules#scheduling-workflows-with-recurring-schedules-for-recipients).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
                    "locale": locale,
                    "name": name,
                    "preferences": preferences,
                    "timezone": timezone,
                },
                object_set_params.ObjectSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Object,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ChannelData:
        """Sets the channel data for the specified object and channel.

        If no object exists
        in the current environment for the given `collection` and `object_id`, Knock
        will create the object as part of this request.

        Args:
          data: Channel data for a given channel type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ChannelData,
        )

    def set_preferences(
        self,
        collection: str,
        object_id: str,
        id: str,
        *,
        _persistence_strategy: Literal["merge", "replace"] | Omit = omit,
        categories: Optional[Dict[str, object_set_preferences_params.Categories]] | Omit = omit,
        channel_types: Optional[PreferenceSetChannelTypesParam] | Omit = omit,
        channels: Optional[Dict[str, object_set_preferences_params.Channels]] | Omit = omit,
        commercial_subscribed: Optional[bool] | Omit = omit,
        workflows: Optional[Dict[str, object_set_preferences_params.Workflows]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PreferenceSet:
        """Sets preferences within the given preference set.

        By default, this is a
        destructive operation and will replace any existing preferences with the
        preferences given. Use '\\__\\__persistence_strategy': 'merge' to merge with
        existing preferences instead. If no object exists in the current environment for
        the given `:collection` and `:object_id`, Knock will create the object as part
        of this request. The preference set `:id` can be either `default` or a
        `tenant.id`. Learn more about
        [per-tenant preferences](/preferences/tenant-preferences).

        Args:
          _persistence_strategy: Controls how the preference set is persisted. 'replace' will completely replace
              the preference set, 'merge' will merge with existing preferences.

          categories: An object where the key is the category and the values are the preference
              settings for that category.

          channel_types: Channel type preferences.

          channels: Channel preferences.

          commercial_subscribed: Whether the recipient is subscribed to commercial communications. When false,
              the recipient will not receive commercial workflow notifications.

          workflows: An object where the key is the workflow key and the values are the preference
              settings for that workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
                    "_persistence_strategy": _persistence_strategy,
                    "categories": categories,
                    "channel_types": channel_types,
                    "channels": channels,
                    "commercial_subscribed": commercial_subscribed,
                    "workflows": workflows,
                },
                object_set_preferences_params.ObjectSetPreferencesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PreferenceSet,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Unsets the channel data for the specified object and channel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/objects/{collection}/{object_id}/channel_data/{channel_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncObjectsResource(AsyncAPIResource):
    """An object represents a resource in your system that you want to map into Knock."""

    @cached_property
    def bulk(self) -> AsyncBulkResource:
        """
        A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
        """
        return AsyncBulkResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncObjectsResourceWithStreamingResponse(self)

    def list(
        self,
        collection: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        include: List[Literal["preferences"]] | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Object, AsyncEntriesCursor[Object]]:
        """Returns a paginated list of objects from the specified collection.

        Optionally
        includes preference data for the objects.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          include: Includes preferences of the objects in the response.

          page_size: The number of items per page (defaults to 50).

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

    async def delete(
        self,
        collection: str,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Permanently removes an object from the specified collection.

        This operation
        cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/objects/{collection}/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def add_subscriptions(
        self,
        collection: str,
        object_id: str,
        *,
        recipients: SequenceNotStr[RecipientRequestParam],
        properties: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ObjectAddSubscriptionsResponse:
        """Add subscriptions for an object.

        If a subscription already exists, it will be
        updated. This endpoint also handles
        [inline identifications](/managing-recipients/identifying-recipients#inline-identifying-recipients)
        for the `recipient`.

        Args:
          recipients: The recipients of the subscription. You can subscribe up to 100 recipients to an
              object at a time.

          properties: The custom properties associated with the subscription relationship.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ObjectAddSubscriptionsResponse,
        )

    async def delete_subscriptions(
        self,
        collection: str,
        object_id: str,
        *,
        recipients: SequenceNotStr[RecipientReferenceParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ObjectDeleteSubscriptionsResponse:
        """Delete subscriptions for the specified recipients from an object.

        Returns the
        list of deleted subscriptions.

        Args:
          recipients: The recipients of the subscription. You can subscribe up to 100 recipients to an
              object at a time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ObjectDeleteSubscriptionsResponse,
        )

    async def get(
        self,
        collection: str,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Object:
        """Retrieves a specific object by its ID from the specified collection.

        Returns the
        object with all its properties.

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
        collection: str,
        object_id: str,
        channel_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    async def get_preferences(
        self,
        collection: str,
        object_id: str,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceSet:
        """
        Returns the preference set for the specified object and preference set `id`.

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/objects/{collection}/{object_id}/preferences/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceSet,
        )

    def list_messages(
        self,
        collection: str,
        id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        channel_id: str | Omit = omit,
        engagement_status: List[
            Literal["seen", "unseen", "read", "unread", "archived", "unarchived", "link_clicked", "interacted"]
        ]
        | Omit = omit,
        inserted_at: object_list_messages_params.InsertedAt | Omit = omit,
        message_ids: SequenceNotStr[str] | Omit = omit,
        page_size: int | Omit = omit,
        source: str | Omit = omit,
        status: List[Literal["queued", "sent", "delivered", "delivery_attempted", "undelivered", "not_sent", "bounced"]]
        | Omit = omit,
        tenant: str | Omit = omit,
        trigger_data: str | Omit = omit,
        workflow_categories: SequenceNotStr[str] | Omit = omit,
        workflow_recipient_run_id: str | Omit = omit,
        workflow_run_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Message, AsyncItemsCursor[Message]]:
        """
        Returns a paginated list of messages for a specific object in the given
        collection. Allows filtering by message status and provides various sorting
        options.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          channel_id: Limits the results to items with the corresponding channel ID.

          engagement_status: Limits the results to messages with the given engagement status.

          message_ids: Limits the results to only the message IDs given (max 50). Note: when using this
              option, the results will be subject to any other filters applied to the query.

          page_size: The number of items per page (defaults to 50).

          source: Limits the results to messages triggered by the given workflow key.

          status: Limits the results to messages with the given delivery status.

          tenant: Limits the results to items with the corresponding tenant.

          trigger_data: Limits the results to only messages that were generated with the given data. See
              [trigger data filtering](/api-reference/overview/trigger-data-filtering) for
              more information.

          workflow_categories: Limits the results to messages related to any of the provided categories.

          workflow_recipient_run_id: Limits the results to messages for a specific recipient's workflow run.

          workflow_run_id: Limits the results to messages associated with the top-level workflow run ID
              returned by the workflow trigger request.

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
            page=AsyncItemsCursor[Message],
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
                        "inserted_at": inserted_at,
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
        collection: str,
        object_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    def list_schedules(
        self,
        collection: str,
        id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        page_size: int | Omit = omit,
        tenant: str | Omit = omit,
        workflow: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Schedule, AsyncEntriesCursor[Schedule]]:
        """
        Returns a paginated list of schedules for an object.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          page_size: The number of items per page (defaults to 50).

          tenant: Filter schedules by tenant id.

          workflow: Filter schedules by workflow id.

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
        collection: str,
        object_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        include: List[Literal["preferences"]] | Omit = omit,
        mode: Literal["recipient", "object"] | Omit = omit,
        objects: Iterable[object_list_subscriptions_params.Object] | Omit = omit,
        page_size: int | Omit = omit,
        recipients: SequenceNotStr[RecipientReferenceParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Subscription, AsyncEntriesCursor[Subscription]]:
        """List subscriptions for an object.

        Either list the recipients that subscribe to
        the provided object, or list the objects that the provided object is subscribed
        to. Determined by the `mode` query parameter.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          include: Additional fields to include in the response.

          mode: Mode of the request. `recipient` to list the objects that the provided object is
              subscribed to, `object` to list the recipients that subscribe to the provided
              object.

          objects: Objects to filter by (only used if mode is `recipient`).

          page_size: The number of items per page (defaults to 50).

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

    async def set(
        self,
        collection: str,
        id: str,
        *,
        channel_data: InlineChannelDataRequestParam | Omit = omit,
        locale: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        preferences: InlinePreferenceSetRequestParam | Omit = omit,
        timezone: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Object:
        """
        Creates a new object or updates an existing one in the specified collection.
        This operation is used to identify objects with their properties, as well as
        optional preferences and channel data.

        Args:
          channel_data: A request to set channel data for a type of channel inline.

          locale: The locale of the object. Used for
              [message localization](/concepts/translations).

          name: An optional name for the object.

          preferences: Inline set preferences for a recipient, where the key is the preference set id.
              Preferences that are set inline will be merged into any existing preferences
              rather than replacing them.

          timezone: The timezone of the object. Must be a
              valid [tz database time zone string](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
              Used
              for [recurring schedules](/concepts/schedules#scheduling-workflows-with-recurring-schedules-for-recipients).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
                    "locale": locale,
                    "name": name,
                    "preferences": preferences,
                    "timezone": timezone,
                },
                object_set_params.ObjectSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Object,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ChannelData:
        """Sets the channel data for the specified object and channel.

        If no object exists
        in the current environment for the given `collection` and `object_id`, Knock
        will create the object as part of this request.

        Args:
          data: Channel data for a given channel type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ChannelData,
        )

    async def set_preferences(
        self,
        collection: str,
        object_id: str,
        id: str,
        *,
        _persistence_strategy: Literal["merge", "replace"] | Omit = omit,
        categories: Optional[Dict[str, object_set_preferences_params.Categories]] | Omit = omit,
        channel_types: Optional[PreferenceSetChannelTypesParam] | Omit = omit,
        channels: Optional[Dict[str, object_set_preferences_params.Channels]] | Omit = omit,
        commercial_subscribed: Optional[bool] | Omit = omit,
        workflows: Optional[Dict[str, object_set_preferences_params.Workflows]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PreferenceSet:
        """Sets preferences within the given preference set.

        By default, this is a
        destructive operation and will replace any existing preferences with the
        preferences given. Use '\\__\\__persistence_strategy': 'merge' to merge with
        existing preferences instead. If no object exists in the current environment for
        the given `:collection` and `:object_id`, Knock will create the object as part
        of this request. The preference set `:id` can be either `default` or a
        `tenant.id`. Learn more about
        [per-tenant preferences](/preferences/tenant-preferences).

        Args:
          _persistence_strategy: Controls how the preference set is persisted. 'replace' will completely replace
              the preference set, 'merge' will merge with existing preferences.

          categories: An object where the key is the category and the values are the preference
              settings for that category.

          channel_types: Channel type preferences.

          channels: Channel preferences.

          commercial_subscribed: Whether the recipient is subscribed to commercial communications. When false,
              the recipient will not receive commercial workflow notifications.

          workflows: An object where the key is the workflow key and the values are the preference
              settings for that workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
                    "_persistence_strategy": _persistence_strategy,
                    "categories": categories,
                    "channel_types": channel_types,
                    "channels": channels,
                    "commercial_subscribed": commercial_subscribed,
                    "workflows": workflows,
                },
                object_set_preferences_params.ObjectSetPreferencesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PreferenceSet,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Unsets the channel data for the specified object and channel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not collection:
            raise ValueError(f"Expected a non-empty value for `collection` but received {collection!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/objects/{collection}/{object_id}/channel_data/{channel_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
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
        """
        A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
        """
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
        """
        A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
        """
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
        """
        A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
        """
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
        """
        A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
        """
        return AsyncBulkResourceWithStreamingResponse(self._objects.bulk)
