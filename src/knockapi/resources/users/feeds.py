# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncEntriesCursor, AsyncEntriesCursor
from ...types.users import feed_list_items_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.users.feed_list_items_response import FeedListItemsResponse
from ...types.users.feed_get_settings_response import FeedGetSettingsResponse

__all__ = ["FeedsResource", "AsyncFeedsResource"]


class FeedsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FeedsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return FeedsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeedsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return FeedsResourceWithStreamingResponse(self)

    def get_settings(
        self,
        user_id: str,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeedGetSettingsResponse:
        """
        Returns the feed settings for a user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/users/{user_id}/feeds/{id}/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedGetSettingsResponse,
        )

    def list_items(
        self,
        user_id: str,
        id: str,
        *,
        after: str | Omit = omit,
        archived: Literal["exclude", "include", "only"] | Omit = omit,
        before: str | Omit = omit,
        exclude: str | Omit = omit,
        has_tenant: bool | Omit = omit,
        inserted_at: feed_list_items_params.InsertedAt | Omit = omit,
        locale: str | Omit = omit,
        page_size: int | Omit = omit,
        source: str | Omit = omit,
        status: Literal["unread", "read", "unseen", "seen", "all"] | Omit = omit,
        tenant: str | Omit = omit,
        trigger_data: str | Omit = omit,
        workflow_categories: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEntriesCursor[FeedListItemsResponse]:
        """
        Returns a paginated list of feed items for a user in reverse chronological
        order, including metadata about the feed. If the user has not yet been
        identified within Knock, an empty feed will be returned.

        You can customize the response using
        [response filters](/integrations/in-app/knock#customizing-api-response-content)
        to exclude or only include specific properties on your resources.

        **Notes:**

        - When making this call from a client-side environment, use your publishable key
          along with a user token.
        - This endpoint’s rate limit is always scoped per-user and per-environment. This
          is true even for requests made without a signed user token.
        - Any [attachments](/integrations/email/attachments) present in trigger data are
          automatically excluded from both the `data` and `activities` fields of
          `UserInAppFeedResponse`.

        Args:
          after: The cursor to fetch entries after.

          archived: The archived status of the feed items.

          before: The cursor to fetch entries before.

          exclude: Comma-separated list of field paths to exclude from the response. Use dot
              notation for nested fields (e.g., `entries.archived_at`). Limited to 3 levels
              deep.

          has_tenant: Whether the feed items have a tenant.

          locale: The locale to render the feed items in. Must be in the IETF 5646 format (e.g.
              `en-US`). When not provided, will default to the locale that the feed items were
              rendered in. Only available for enterprise plan customers using custom
              translations.

          page_size: The number of items per page (defaults to 50).

          source: The workflow key associated with the message in the feed.

          status: The status of the feed items.

          tenant: The tenant associated with the feed items.

          trigger_data: The trigger data of the feed items (as a JSON string).

          workflow_categories: The workflow categories of the feed items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            f"/v1/users/{user_id}/feeds/{id}",
            page=SyncEntriesCursor[FeedListItemsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "before": before,
                        "exclude": exclude,
                        "has_tenant": has_tenant,
                        "inserted_at": inserted_at,
                        "locale": locale,
                        "page_size": page_size,
                        "source": source,
                        "status": status,
                        "tenant": tenant,
                        "trigger_data": trigger_data,
                        "workflow_categories": workflow_categories,
                    },
                    feed_list_items_params.FeedListItemsParams,
                ),
            ),
            model=FeedListItemsResponse,
        )


class AsyncFeedsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFeedsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeedsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeedsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncFeedsResourceWithStreamingResponse(self)

    async def get_settings(
        self,
        user_id: str,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeedGetSettingsResponse:
        """
        Returns the feed settings for a user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/users/{user_id}/feeds/{id}/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedGetSettingsResponse,
        )

    def list_items(
        self,
        user_id: str,
        id: str,
        *,
        after: str | Omit = omit,
        archived: Literal["exclude", "include", "only"] | Omit = omit,
        before: str | Omit = omit,
        exclude: str | Omit = omit,
        has_tenant: bool | Omit = omit,
        inserted_at: feed_list_items_params.InsertedAt | Omit = omit,
        locale: str | Omit = omit,
        page_size: int | Omit = omit,
        source: str | Omit = omit,
        status: Literal["unread", "read", "unseen", "seen", "all"] | Omit = omit,
        tenant: str | Omit = omit,
        trigger_data: str | Omit = omit,
        workflow_categories: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[FeedListItemsResponse, AsyncEntriesCursor[FeedListItemsResponse]]:
        """
        Returns a paginated list of feed items for a user in reverse chronological
        order, including metadata about the feed. If the user has not yet been
        identified within Knock, an empty feed will be returned.

        You can customize the response using
        [response filters](/integrations/in-app/knock#customizing-api-response-content)
        to exclude or only include specific properties on your resources.

        **Notes:**

        - When making this call from a client-side environment, use your publishable key
          along with a user token.
        - This endpoint’s rate limit is always scoped per-user and per-environment. This
          is true even for requests made without a signed user token.
        - Any [attachments](/integrations/email/attachments) present in trigger data are
          automatically excluded from both the `data` and `activities` fields of
          `UserInAppFeedResponse`.

        Args:
          after: The cursor to fetch entries after.

          archived: The archived status of the feed items.

          before: The cursor to fetch entries before.

          exclude: Comma-separated list of field paths to exclude from the response. Use dot
              notation for nested fields (e.g., `entries.archived_at`). Limited to 3 levels
              deep.

          has_tenant: Whether the feed items have a tenant.

          locale: The locale to render the feed items in. Must be in the IETF 5646 format (e.g.
              `en-US`). When not provided, will default to the locale that the feed items were
              rendered in. Only available for enterprise plan customers using custom
              translations.

          page_size: The number of items per page (defaults to 50).

          source: The workflow key associated with the message in the feed.

          status: The status of the feed items.

          tenant: The tenant associated with the feed items.

          trigger_data: The trigger data of the feed items (as a JSON string).

          workflow_categories: The workflow categories of the feed items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            f"/v1/users/{user_id}/feeds/{id}",
            page=AsyncEntriesCursor[FeedListItemsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "before": before,
                        "exclude": exclude,
                        "has_tenant": has_tenant,
                        "inserted_at": inserted_at,
                        "locale": locale,
                        "page_size": page_size,
                        "source": source,
                        "status": status,
                        "tenant": tenant,
                        "trigger_data": trigger_data,
                        "workflow_categories": workflow_categories,
                    },
                    feed_list_items_params.FeedListItemsParams,
                ),
            ),
            model=FeedListItemsResponse,
        )


class FeedsResourceWithRawResponse:
    def __init__(self, feeds: FeedsResource) -> None:
        self._feeds = feeds

        self.get_settings = to_raw_response_wrapper(
            feeds.get_settings,
        )
        self.list_items = to_raw_response_wrapper(
            feeds.list_items,
        )


class AsyncFeedsResourceWithRawResponse:
    def __init__(self, feeds: AsyncFeedsResource) -> None:
        self._feeds = feeds

        self.get_settings = async_to_raw_response_wrapper(
            feeds.get_settings,
        )
        self.list_items = async_to_raw_response_wrapper(
            feeds.list_items,
        )


class FeedsResourceWithStreamingResponse:
    def __init__(self, feeds: FeedsResource) -> None:
        self._feeds = feeds

        self.get_settings = to_streamed_response_wrapper(
            feeds.get_settings,
        )
        self.list_items = to_streamed_response_wrapper(
            feeds.list_items,
        )


class AsyncFeedsResourceWithStreamingResponse:
    def __init__(self, feeds: AsyncFeedsResource) -> None:
        self._feeds = feeds

        self.get_settings = async_to_streamed_response_wrapper(
            feeds.get_settings,
        )
        self.list_items = async_to_streamed_response_wrapper(
            feeds.list_items,
        )
