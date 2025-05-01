# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
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
from ...types.activity import Activity
from ...types.messages import activity_list_params

__all__ = ["ActivitiesResource", "AsyncActivitiesResource"]


class ActivitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActivitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return ActivitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActivitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return ActivitiesResourceWithStreamingResponse(self)

    def list(
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
                    activity_list_params.ActivityListParams,
                ),
            ),
            model=Activity,
        )


class AsyncActivitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActivitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActivitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActivitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncActivitiesResourceWithStreamingResponse(self)

    def list(
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
                    activity_list_params.ActivityListParams,
                ),
            ),
            model=Activity,
        )


class ActivitiesResourceWithRawResponse:
    def __init__(self, activities: ActivitiesResource) -> None:
        self._activities = activities

        self.list = to_raw_response_wrapper(
            activities.list,
        )


class AsyncActivitiesResourceWithRawResponse:
    def __init__(self, activities: AsyncActivitiesResource) -> None:
        self._activities = activities

        self.list = async_to_raw_response_wrapper(
            activities.list,
        )


class ActivitiesResourceWithStreamingResponse:
    def __init__(self, activities: ActivitiesResource) -> None:
        self._activities = activities

        self.list = to_streamed_response_wrapper(
            activities.list,
        )


class AsyncActivitiesResourceWithStreamingResponse:
    def __init__(self, activities: AsyncActivitiesResource) -> None:
        self._activities = activities

        self.list = async_to_streamed_response_wrapper(
            activities.list,
        )
