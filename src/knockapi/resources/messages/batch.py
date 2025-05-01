# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

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
from ...types.messages import (
    batch_archive_params,
    batch_unarchive_params,
    batch_get_content_params,
    batch_mark_as_read_params,
    batch_mark_as_seen_params,
    batch_mark_as_unread_params,
    batch_mark_as_unseen_params,
    batch_mark_as_interacted_params,
)
from ...types.messages.batch_archive_response import BatchArchiveResponse
from ...types.messages.batch_unarchive_response import BatchUnarchiveResponse
from ...types.messages.batch_get_content_response import BatchGetContentResponse
from ...types.messages.batch_mark_as_read_response import BatchMarkAsReadResponse
from ...types.messages.batch_mark_as_seen_response import BatchMarkAsSeenResponse
from ...types.messages.batch_mark_as_unread_response import BatchMarkAsUnreadResponse
from ...types.messages.batch_mark_as_unseen_response import BatchMarkAsUnseenResponse
from ...types.messages.batch_mark_as_interacted_response import BatchMarkAsInteractedResponse

__all__ = ["BatchResource", "AsyncBatchResource"]


class BatchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return BatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return BatchResourceWithStreamingResponse(self)

    def archive(
        self,
        *,
        message_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchArchiveResponse:
        """Marks the given messages as archived.

        Archived messages are hidden from the
        default message list in the feed but can still be accessed and unarchived later.

        Args:
          message_ids: The message IDs to update the status of.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/messages/batch/archived",
            body=maybe_transform({"message_ids": message_ids}, batch_archive_params.BatchArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchArchiveResponse,
        )

    def get_content(
        self,
        *,
        message_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchGetContentResponse:
        """
        Get the contents of multiple messages in a single request.

        Args:
          message_ids: The IDs of the messages to fetch contents of.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/messages/batch/content",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"message_ids": message_ids}, batch_get_content_params.BatchGetContentParams),
            ),
            cast_to=BatchGetContentResponse,
        )

    def mark_as_interacted(
        self,
        *,
        message_ids: List[str],
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchMarkAsInteractedResponse:
        """Marks the given messages as interacted with by the user.

        This can include any
        user action on the message, with optional metadata about the specific
        interaction. Cannot include more than 5 key-value pairs, must not contain nested
        data. Read more about message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          message_ids: The message IDs to batch mark as interacted with.

          metadata: Metadata about the interaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/messages/batch/interacted",
            body=maybe_transform(
                {
                    "message_ids": message_ids,
                    "metadata": metadata,
                },
                batch_mark_as_interacted_params.BatchMarkAsInteractedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchMarkAsInteractedResponse,
        )

    def mark_as_read(
        self,
        *,
        message_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchMarkAsReadResponse:
        """Marks the given messages as `read`.

        Read more about message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          message_ids: The message IDs to update the status of.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/messages/batch/read",
            body=maybe_transform({"message_ids": message_ids}, batch_mark_as_read_params.BatchMarkAsReadParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchMarkAsReadResponse,
        )

    def mark_as_seen(
        self,
        *,
        message_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchMarkAsSeenResponse:
        """Marks the given messages as `seen`.

        This indicates that the user has viewed the
        message in their feed or inbox. Read more about message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          message_ids: The message IDs to update the status of.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/messages/batch/seen",
            body=maybe_transform({"message_ids": message_ids}, batch_mark_as_seen_params.BatchMarkAsSeenParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchMarkAsSeenResponse,
        )

    def mark_as_unread(
        self,
        *,
        message_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchMarkAsUnreadResponse:
        """Marks the given messages as `unread`.

        This reverses the `read` state. Read more
        about message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          message_ids: The message IDs to update the status of.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/messages/batch/unread",
            body=maybe_transform({"message_ids": message_ids}, batch_mark_as_unread_params.BatchMarkAsUnreadParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchMarkAsUnreadResponse,
        )

    def mark_as_unseen(
        self,
        *,
        message_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchMarkAsUnseenResponse:
        """Marks the given messages as `unseen`.

        This reverses the `seen` state. Read more
        about message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          message_ids: The message IDs to update the status of.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/messages/batch/unseen",
            body=maybe_transform({"message_ids": message_ids}, batch_mark_as_unseen_params.BatchMarkAsUnseenParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchMarkAsUnseenResponse,
        )

    def unarchive(
        self,
        *,
        message_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchUnarchiveResponse:
        """Marks the given messages as unarchived.

        This reverses the `archived` state.
        Archived messages are hidden from the default message list in the feed but can
        still be accessed and unarchived later.

        Args:
          message_ids: The message IDs to update the status of.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/messages/batch/unarchived",
            body=maybe_transform({"message_ids": message_ids}, batch_unarchive_params.BatchUnarchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchUnarchiveResponse,
        )


class AsyncBatchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncBatchResourceWithStreamingResponse(self)

    async def archive(
        self,
        *,
        message_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchArchiveResponse:
        """Marks the given messages as archived.

        Archived messages are hidden from the
        default message list in the feed but can still be accessed and unarchived later.

        Args:
          message_ids: The message IDs to update the status of.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/messages/batch/archived",
            body=await async_maybe_transform({"message_ids": message_ids}, batch_archive_params.BatchArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchArchiveResponse,
        )

    async def get_content(
        self,
        *,
        message_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchGetContentResponse:
        """
        Get the contents of multiple messages in a single request.

        Args:
          message_ids: The IDs of the messages to fetch contents of.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/messages/batch/content",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"message_ids": message_ids}, batch_get_content_params.BatchGetContentParams
                ),
            ),
            cast_to=BatchGetContentResponse,
        )

    async def mark_as_interacted(
        self,
        *,
        message_ids: List[str],
        metadata: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchMarkAsInteractedResponse:
        """Marks the given messages as interacted with by the user.

        This can include any
        user action on the message, with optional metadata about the specific
        interaction. Cannot include more than 5 key-value pairs, must not contain nested
        data. Read more about message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          message_ids: The message IDs to batch mark as interacted with.

          metadata: Metadata about the interaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/messages/batch/interacted",
            body=await async_maybe_transform(
                {
                    "message_ids": message_ids,
                    "metadata": metadata,
                },
                batch_mark_as_interacted_params.BatchMarkAsInteractedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchMarkAsInteractedResponse,
        )

    async def mark_as_read(
        self,
        *,
        message_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchMarkAsReadResponse:
        """Marks the given messages as `read`.

        Read more about message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          message_ids: The message IDs to update the status of.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/messages/batch/read",
            body=await async_maybe_transform(
                {"message_ids": message_ids}, batch_mark_as_read_params.BatchMarkAsReadParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchMarkAsReadResponse,
        )

    async def mark_as_seen(
        self,
        *,
        message_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchMarkAsSeenResponse:
        """Marks the given messages as `seen`.

        This indicates that the user has viewed the
        message in their feed or inbox. Read more about message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          message_ids: The message IDs to update the status of.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/messages/batch/seen",
            body=await async_maybe_transform(
                {"message_ids": message_ids}, batch_mark_as_seen_params.BatchMarkAsSeenParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchMarkAsSeenResponse,
        )

    async def mark_as_unread(
        self,
        *,
        message_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchMarkAsUnreadResponse:
        """Marks the given messages as `unread`.

        This reverses the `read` state. Read more
        about message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          message_ids: The message IDs to update the status of.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/messages/batch/unread",
            body=await async_maybe_transform(
                {"message_ids": message_ids}, batch_mark_as_unread_params.BatchMarkAsUnreadParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchMarkAsUnreadResponse,
        )

    async def mark_as_unseen(
        self,
        *,
        message_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchMarkAsUnseenResponse:
        """Marks the given messages as `unseen`.

        This reverses the `seen` state. Read more
        about message engagement statuses
        [here](/send-notifications/message-statuses#engagement-status).

        Args:
          message_ids: The message IDs to update the status of.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/messages/batch/unseen",
            body=await async_maybe_transform(
                {"message_ids": message_ids}, batch_mark_as_unseen_params.BatchMarkAsUnseenParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchMarkAsUnseenResponse,
        )

    async def unarchive(
        self,
        *,
        message_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchUnarchiveResponse:
        """Marks the given messages as unarchived.

        This reverses the `archived` state.
        Archived messages are hidden from the default message list in the feed but can
        still be accessed and unarchived later.

        Args:
          message_ids: The message IDs to update the status of.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/messages/batch/unarchived",
            body=await async_maybe_transform({"message_ids": message_ids}, batch_unarchive_params.BatchUnarchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchUnarchiveResponse,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.archive = to_raw_response_wrapper(
            batch.archive,
        )
        self.get_content = to_raw_response_wrapper(
            batch.get_content,
        )
        self.mark_as_interacted = to_raw_response_wrapper(
            batch.mark_as_interacted,
        )
        self.mark_as_read = to_raw_response_wrapper(
            batch.mark_as_read,
        )
        self.mark_as_seen = to_raw_response_wrapper(
            batch.mark_as_seen,
        )
        self.mark_as_unread = to_raw_response_wrapper(
            batch.mark_as_unread,
        )
        self.mark_as_unseen = to_raw_response_wrapper(
            batch.mark_as_unseen,
        )
        self.unarchive = to_raw_response_wrapper(
            batch.unarchive,
        )


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.archive = async_to_raw_response_wrapper(
            batch.archive,
        )
        self.get_content = async_to_raw_response_wrapper(
            batch.get_content,
        )
        self.mark_as_interacted = async_to_raw_response_wrapper(
            batch.mark_as_interacted,
        )
        self.mark_as_read = async_to_raw_response_wrapper(
            batch.mark_as_read,
        )
        self.mark_as_seen = async_to_raw_response_wrapper(
            batch.mark_as_seen,
        )
        self.mark_as_unread = async_to_raw_response_wrapper(
            batch.mark_as_unread,
        )
        self.mark_as_unseen = async_to_raw_response_wrapper(
            batch.mark_as_unseen,
        )
        self.unarchive = async_to_raw_response_wrapper(
            batch.unarchive,
        )


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.archive = to_streamed_response_wrapper(
            batch.archive,
        )
        self.get_content = to_streamed_response_wrapper(
            batch.get_content,
        )
        self.mark_as_interacted = to_streamed_response_wrapper(
            batch.mark_as_interacted,
        )
        self.mark_as_read = to_streamed_response_wrapper(
            batch.mark_as_read,
        )
        self.mark_as_seen = to_streamed_response_wrapper(
            batch.mark_as_seen,
        )
        self.mark_as_unread = to_streamed_response_wrapper(
            batch.mark_as_unread,
        )
        self.mark_as_unseen = to_streamed_response_wrapper(
            batch.mark_as_unseen,
        )
        self.unarchive = to_streamed_response_wrapper(
            batch.unarchive,
        )


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.archive = async_to_streamed_response_wrapper(
            batch.archive,
        )
        self.get_content = async_to_streamed_response_wrapper(
            batch.get_content,
        )
        self.mark_as_interacted = async_to_streamed_response_wrapper(
            batch.mark_as_interacted,
        )
        self.mark_as_read = async_to_streamed_response_wrapper(
            batch.mark_as_read,
        )
        self.mark_as_seen = async_to_streamed_response_wrapper(
            batch.mark_as_seen,
        )
        self.mark_as_unread = async_to_streamed_response_wrapper(
            batch.mark_as_unread,
        )
        self.mark_as_unseen = async_to_streamed_response_wrapper(
            batch.mark_as_unseen,
        )
        self.unarchive = async_to_streamed_response_wrapper(
            batch.unarchive,
        )
