# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from ...types import (
    message_list_params,
    message_list_events_params,
    message_list_activities_params,
    message_list_delivery_logs_params,
    message_mark_as_interacted_params,
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
from ...pagination import SyncItemsCursor, AsyncItemsCursor
from ..._base_client import AsyncPaginator, make_request_options
from ...types.message import Message
from ...types.activity import Activity
from ...types.message_event import MessageEvent
from ...types.message_delivery_log import MessageDeliveryLog
from ...types.message_get_content_response import MessageGetContentResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        channel_id: str | NotGiven = NOT_GIVEN,
        engagement_status: List[
            Literal["seen", "unseen", "read", "unread", "archived", "unarchived", "link_clicked", "interacted"]
        ]
        | NotGiven = NOT_GIVEN,
        inserted_at: message_list_params.InsertedAt | NotGiven = NOT_GIVEN,
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
    ) -> SyncItemsCursor[Message]:
        """
        Returns a paginated list of messages for the current environment.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          channel_id: Limits the results to items with the corresponding channel ID.

          engagement_status: Limits the results to messages with the given engagement status.

          message_ids: Limits the results to only the message IDs given (max 50). Note: when using this
              option, the results will be subject to any other filters applied to the query.

          page_size: The number of items per page.

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
        return self._get_api_list(
            "/v1/messages",
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
                    message_list_params.MessageListParams,
                ),
            ),
            model=Message,
        )

    def archive(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """Archives a message for the user.

        Archived messages are hidden from the default
        message list in the feed but can still be accessed and unarchived later.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._put(
            f"/v1/messages/{message_id}/archived",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    def get(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """
        Retrieves a specific message by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            f"/v1/messages/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    def get_content(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageGetContentResponse:
        """
        Returns the fully rendered contents of a message, where the response depends on
        which channel the message was sent through.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            f"/v1/messages/{message_id}/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageGetContentResponse,
        )

    def list_activities(
        self,
        message_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        trigger_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncItemsCursor[Activity]:
        """
        Returns a paginated list of activities for the specified message.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          page_size: The number of items per page.

          trigger_data: The trigger data to filter activities by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get_api_list(
            f"/v1/messages/{message_id}/activities",
            page=SyncItemsCursor[Activity],
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
                        "trigger_data": trigger_data,
                    },
                    message_list_activities_params.MessageListActivitiesParams,
                ),
            ),
            model=Activity,
        )

    def list_delivery_logs(
        self,
        message_id: str,
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
    ) -> SyncItemsCursor[MessageDeliveryLog]:
        """
        Returns a paginated list of delivery logs for the specified message.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          page_size: The number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get_api_list(
            f"/v1/messages/{message_id}/delivery_logs",
            page=SyncItemsCursor[MessageDeliveryLog],
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
                    message_list_delivery_logs_params.MessageListDeliveryLogsParams,
                ),
            ),
            model=MessageDeliveryLog,
        )

    def list_events(
        self,
        message_id: str,
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
    ) -> SyncItemsCursor[MessageEvent]:
        """
        Returns a paginated list of events for the specified message.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          page_size: The number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get_api_list(
            f"/v1/messages/{message_id}/events",
            page=SyncItemsCursor[MessageEvent],
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
                    message_list_events_params.MessageListEventsParams,
                ),
            ),
            model=MessageEvent,
        )

    def mark_as_interacted(
        self,
        message_id: str,
        *,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """Marks a message as `interacted` with by the user.

        This can include any user
        action on the message, with optional metadata about the specific interaction.
        Cannot include more than 5 key-value pairs, must not contain nested data. Read
        more about message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          metadata: Metadata about the interaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._put(
            f"/v1/messages/{message_id}/interacted",
            body=maybe_transform(
                {"metadata": metadata}, message_mark_as_interacted_params.MessageMarkAsInteractedParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    def mark_as_read(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """Marks a message as `read`.

        This indicates that the user has read the message
        content. Read more about message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._put(
            f"/v1/messages/{message_id}/read",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    def mark_as_seen(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """Marks a message as `seen`.

        This indicates that the user has viewed the message
        in their feed or inbox. Read more about message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._put(
            f"/v1/messages/{message_id}/seen",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    def mark_as_unread(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """Marks a message as `unread`.

        This reverses the `read` state. Read more about
        message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._delete(
            f"/v1/messages/{message_id}/read",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    def mark_as_unseen(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """Marks a message as `unseen`.

        This reverses the `seen` state. Read more about
        message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._delete(
            f"/v1/messages/{message_id}/seen",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    def unarchive(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """
        Removes a message from the archived state, making it visible in the default
        message list in the feed again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._delete(
            f"/v1/messages/{message_id}/archived",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        channel_id: str | NotGiven = NOT_GIVEN,
        engagement_status: List[
            Literal["seen", "unseen", "read", "unread", "archived", "unarchived", "link_clicked", "interacted"]
        ]
        | NotGiven = NOT_GIVEN,
        inserted_at: message_list_params.InsertedAt | NotGiven = NOT_GIVEN,
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
    ) -> AsyncPaginator[Message, AsyncItemsCursor[Message]]:
        """
        Returns a paginated list of messages for the current environment.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          channel_id: Limits the results to items with the corresponding channel ID.

          engagement_status: Limits the results to messages with the given engagement status.

          message_ids: Limits the results to only the message IDs given (max 50). Note: when using this
              option, the results will be subject to any other filters applied to the query.

          page_size: The number of items per page.

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
        return self._get_api_list(
            "/v1/messages",
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
                    message_list_params.MessageListParams,
                ),
            ),
            model=Message,
        )

    async def archive(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """Archives a message for the user.

        Archived messages are hidden from the default
        message list in the feed but can still be accessed and unarchived later.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._put(
            f"/v1/messages/{message_id}/archived",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    async def get(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """
        Retrieves a specific message by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            f"/v1/messages/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    async def get_content(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageGetContentResponse:
        """
        Returns the fully rendered contents of a message, where the response depends on
        which channel the message was sent through.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            f"/v1/messages/{message_id}/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageGetContentResponse,
        )

    def list_activities(
        self,
        message_id: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        trigger_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Activity, AsyncItemsCursor[Activity]]:
        """
        Returns a paginated list of activities for the specified message.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          page_size: The number of items per page.

          trigger_data: The trigger data to filter activities by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get_api_list(
            f"/v1/messages/{message_id}/activities",
            page=AsyncItemsCursor[Activity],
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
                        "trigger_data": trigger_data,
                    },
                    message_list_activities_params.MessageListActivitiesParams,
                ),
            ),
            model=Activity,
        )

    def list_delivery_logs(
        self,
        message_id: str,
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
    ) -> AsyncPaginator[MessageDeliveryLog, AsyncItemsCursor[MessageDeliveryLog]]:
        """
        Returns a paginated list of delivery logs for the specified message.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          page_size: The number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get_api_list(
            f"/v1/messages/{message_id}/delivery_logs",
            page=AsyncItemsCursor[MessageDeliveryLog],
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
                    message_list_delivery_logs_params.MessageListDeliveryLogsParams,
                ),
            ),
            model=MessageDeliveryLog,
        )

    def list_events(
        self,
        message_id: str,
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
    ) -> AsyncPaginator[MessageEvent, AsyncItemsCursor[MessageEvent]]:
        """
        Returns a paginated list of events for the specified message.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          page_size: The number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get_api_list(
            f"/v1/messages/{message_id}/events",
            page=AsyncItemsCursor[MessageEvent],
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
                    message_list_events_params.MessageListEventsParams,
                ),
            ),
            model=MessageEvent,
        )

    async def mark_as_interacted(
        self,
        message_id: str,
        *,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """Marks a message as `interacted` with by the user.

        This can include any user
        action on the message, with optional metadata about the specific interaction.
        Cannot include more than 5 key-value pairs, must not contain nested data. Read
        more about message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          metadata: Metadata about the interaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._put(
            f"/v1/messages/{message_id}/interacted",
            body=await async_maybe_transform(
                {"metadata": metadata}, message_mark_as_interacted_params.MessageMarkAsInteractedParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    async def mark_as_read(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """Marks a message as `read`.

        This indicates that the user has read the message
        content. Read more about message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._put(
            f"/v1/messages/{message_id}/read",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    async def mark_as_seen(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """Marks a message as `seen`.

        This indicates that the user has viewed the message
        in their feed or inbox. Read more about message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._put(
            f"/v1/messages/{message_id}/seen",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    async def mark_as_unread(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """Marks a message as `unread`.

        This reverses the `read` state. Read more about
        message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._delete(
            f"/v1/messages/{message_id}/read",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    async def mark_as_unseen(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """Marks a message as `unseen`.

        This reverses the `seen` state. Read more about
        message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._delete(
            f"/v1/messages/{message_id}/seen",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )

    async def unarchive(
        self,
        message_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Message:
        """
        Removes a message from the archived state, making it visible in the default
        message list in the feed again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._delete(
            f"/v1/messages/{message_id}/archived",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Message,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.archive = to_raw_response_wrapper(
            messages.archive,
        )
        self.get = to_raw_response_wrapper(
            messages.get,
        )
        self.get_content = to_raw_response_wrapper(
            messages.get_content,
        )
        self.list_activities = to_raw_response_wrapper(
            messages.list_activities,
        )
        self.list_delivery_logs = to_raw_response_wrapper(
            messages.list_delivery_logs,
        )
        self.list_events = to_raw_response_wrapper(
            messages.list_events,
        )
        self.mark_as_interacted = to_raw_response_wrapper(
            messages.mark_as_interacted,
        )
        self.mark_as_read = to_raw_response_wrapper(
            messages.mark_as_read,
        )
        self.mark_as_seen = to_raw_response_wrapper(
            messages.mark_as_seen,
        )
        self.mark_as_unread = to_raw_response_wrapper(
            messages.mark_as_unread,
        )
        self.mark_as_unseen = to_raw_response_wrapper(
            messages.mark_as_unseen,
        )
        self.unarchive = to_raw_response_wrapper(
            messages.unarchive,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._messages.batch)


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.archive = async_to_raw_response_wrapper(
            messages.archive,
        )
        self.get = async_to_raw_response_wrapper(
            messages.get,
        )
        self.get_content = async_to_raw_response_wrapper(
            messages.get_content,
        )
        self.list_activities = async_to_raw_response_wrapper(
            messages.list_activities,
        )
        self.list_delivery_logs = async_to_raw_response_wrapper(
            messages.list_delivery_logs,
        )
        self.list_events = async_to_raw_response_wrapper(
            messages.list_events,
        )
        self.mark_as_interacted = async_to_raw_response_wrapper(
            messages.mark_as_interacted,
        )
        self.mark_as_read = async_to_raw_response_wrapper(
            messages.mark_as_read,
        )
        self.mark_as_seen = async_to_raw_response_wrapper(
            messages.mark_as_seen,
        )
        self.mark_as_unread = async_to_raw_response_wrapper(
            messages.mark_as_unread,
        )
        self.mark_as_unseen = async_to_raw_response_wrapper(
            messages.mark_as_unseen,
        )
        self.unarchive = async_to_raw_response_wrapper(
            messages.unarchive,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._messages.batch)


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.archive = to_streamed_response_wrapper(
            messages.archive,
        )
        self.get = to_streamed_response_wrapper(
            messages.get,
        )
        self.get_content = to_streamed_response_wrapper(
            messages.get_content,
        )
        self.list_activities = to_streamed_response_wrapper(
            messages.list_activities,
        )
        self.list_delivery_logs = to_streamed_response_wrapper(
            messages.list_delivery_logs,
        )
        self.list_events = to_streamed_response_wrapper(
            messages.list_events,
        )
        self.mark_as_interacted = to_streamed_response_wrapper(
            messages.mark_as_interacted,
        )
        self.mark_as_read = to_streamed_response_wrapper(
            messages.mark_as_read,
        )
        self.mark_as_seen = to_streamed_response_wrapper(
            messages.mark_as_seen,
        )
        self.mark_as_unread = to_streamed_response_wrapper(
            messages.mark_as_unread,
        )
        self.mark_as_unseen = to_streamed_response_wrapper(
            messages.mark_as_unseen,
        )
        self.unarchive = to_streamed_response_wrapper(
            messages.unarchive,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._messages.batch)


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            messages.archive,
        )
        self.get = async_to_streamed_response_wrapper(
            messages.get,
        )
        self.get_content = async_to_streamed_response_wrapper(
            messages.get_content,
        )
        self.list_activities = async_to_streamed_response_wrapper(
            messages.list_activities,
        )
        self.list_delivery_logs = async_to_streamed_response_wrapper(
            messages.list_delivery_logs,
        )
        self.list_events = async_to_streamed_response_wrapper(
            messages.list_events,
        )
        self.mark_as_interacted = async_to_streamed_response_wrapper(
            messages.mark_as_interacted,
        )
        self.mark_as_read = async_to_streamed_response_wrapper(
            messages.mark_as_read,
        )
        self.mark_as_seen = async_to_streamed_response_wrapper(
            messages.mark_as_seen,
        )
        self.mark_as_unread = async_to_streamed_response_wrapper(
            messages.mark_as_unread,
        )
        self.mark_as_unseen = async_to_streamed_response_wrapper(
            messages.mark_as_unseen,
        )
        self.unarchive = async_to_streamed_response_wrapper(
            messages.unarchive,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._messages.batch)
