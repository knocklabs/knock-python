# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

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
from ...types.channels import bulk_update_message_status_params
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

    def update_message_status(
        self,
        channel_id: str,
        action: Literal[
            "seen", "unseen", "read", "unread", "archived", "unarchived", "interacted", "archive", "unarchive", "delete"
        ],
        *,
        archived: Literal["exclude", "include", "only"] | NotGiven = NOT_GIVEN,
        delivery_status: Literal[
            "queued", "sent", "delivered", "delivery_attempted", "undelivered", "not_sent", "bounced"
        ]
        | NotGiven = NOT_GIVEN,
        engagement_status: Literal[
            "seen", "unseen", "read", "unread", "archived", "unarchived", "link_clicked", "interacted"
        ]
        | NotGiven = NOT_GIVEN,
        has_tenant: bool | NotGiven = NOT_GIVEN,
        newer_than: Union[str, datetime] | NotGiven = NOT_GIVEN,
        older_than: Union[str, datetime] | NotGiven = NOT_GIVEN,
        recipient_ids: List[str] | NotGiven = NOT_GIVEN,
        tenants: List[str] | NotGiven = NOT_GIVEN,
        trigger_data: str | NotGiven = NOT_GIVEN,
        workflows: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkOperation:
        """Bulk update the status of messages for a specific channel.

        The channel is
        specified by the `channel_id` parameter. The action to perform is specified by
        the `action` parameter, where the action is a status change action (e.g.
        `archive`, `unarchive`).

        Args:
          archived: Limits the results to messages with the given archived status.

          delivery_status: Limits the results to messages with the given delivery status.

          engagement_status: Limits the results to messages with the given engagement status.

          has_tenant: Limits the results to messages that have a tenant or not.

          newer_than: Limits the results to messages inserted after the given date.

          older_than: Limits the results to messages inserted before the given date.

          recipient_ids: Limits the results to messages with the given recipient IDs.

          tenants: Limits the results to messages with the given tenant IDs.

          trigger_data: Limits the results to only messages that were generated with the given data. See
              [trigger data filtering](/api-reference/overview/trigger-data-filtering) for
              more information.

          workflows: Limits the results to messages with the given workflow keys.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        return self._post(
            f"/v1/channels/{channel_id}/messages/bulk/{action}",
            body=maybe_transform(
                {
                    "archived": archived,
                    "delivery_status": delivery_status,
                    "engagement_status": engagement_status,
                    "has_tenant": has_tenant,
                    "newer_than": newer_than,
                    "older_than": older_than,
                    "recipient_ids": recipient_ids,
                    "tenants": tenants,
                    "trigger_data": trigger_data,
                    "workflows": workflows,
                },
                bulk_update_message_status_params.BulkUpdateMessageStatusParams,
            ),
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

    async def update_message_status(
        self,
        channel_id: str,
        action: Literal[
            "seen", "unseen", "read", "unread", "archived", "unarchived", "interacted", "archive", "unarchive", "delete"
        ],
        *,
        archived: Literal["exclude", "include", "only"] | NotGiven = NOT_GIVEN,
        delivery_status: Literal[
            "queued", "sent", "delivered", "delivery_attempted", "undelivered", "not_sent", "bounced"
        ]
        | NotGiven = NOT_GIVEN,
        engagement_status: Literal[
            "seen", "unseen", "read", "unread", "archived", "unarchived", "link_clicked", "interacted"
        ]
        | NotGiven = NOT_GIVEN,
        has_tenant: bool | NotGiven = NOT_GIVEN,
        newer_than: Union[str, datetime] | NotGiven = NOT_GIVEN,
        older_than: Union[str, datetime] | NotGiven = NOT_GIVEN,
        recipient_ids: List[str] | NotGiven = NOT_GIVEN,
        tenants: List[str] | NotGiven = NOT_GIVEN,
        trigger_data: str | NotGiven = NOT_GIVEN,
        workflows: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkOperation:
        """Bulk update the status of messages for a specific channel.

        The channel is
        specified by the `channel_id` parameter. The action to perform is specified by
        the `action` parameter, where the action is a status change action (e.g.
        `archive`, `unarchive`).

        Args:
          archived: Limits the results to messages with the given archived status.

          delivery_status: Limits the results to messages with the given delivery status.

          engagement_status: Limits the results to messages with the given engagement status.

          has_tenant: Limits the results to messages that have a tenant or not.

          newer_than: Limits the results to messages inserted after the given date.

          older_than: Limits the results to messages inserted before the given date.

          recipient_ids: Limits the results to messages with the given recipient IDs.

          tenants: Limits the results to messages with the given tenant IDs.

          trigger_data: Limits the results to only messages that were generated with the given data. See
              [trigger data filtering](/api-reference/overview/trigger-data-filtering) for
              more information.

          workflows: Limits the results to messages with the given workflow keys.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        return await self._post(
            f"/v1/channels/{channel_id}/messages/bulk/{action}",
            body=await async_maybe_transform(
                {
                    "archived": archived,
                    "delivery_status": delivery_status,
                    "engagement_status": engagement_status,
                    "has_tenant": has_tenant,
                    "newer_than": newer_than,
                    "older_than": older_than,
                    "recipient_ids": recipient_ids,
                    "tenants": tenants,
                    "trigger_data": trigger_data,
                    "workflows": workflows,
                },
                bulk_update_message_status_params.BulkUpdateMessageStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkOperation,
        )


class BulkResourceWithRawResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.update_message_status = to_raw_response_wrapper(
            bulk.update_message_status,
        )


class AsyncBulkResourceWithRawResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.update_message_status = async_to_raw_response_wrapper(
            bulk.update_message_status,
        )


class BulkResourceWithStreamingResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.update_message_status = to_streamed_response_wrapper(
            bulk.update_message_status,
        )


class AsyncBulkResourceWithStreamingResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.update_message_status = async_to_streamed_response_wrapper(
            bulk.update_message_status,
        )
