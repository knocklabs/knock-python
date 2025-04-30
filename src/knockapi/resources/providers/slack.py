# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...pagination import SyncSlackChannelsCursor, AsyncSlackChannelsCursor
from ..._base_client import AsyncPaginator, make_request_options
from ...types.providers import slack_check_auth_params, slack_list_channels_params, slack_revoke_access_params
from ...types.providers.slack_check_auth_response import SlackCheckAuthResponse
from ...types.providers.slack_list_channels_response import SlackListChannelsResponse
from ...types.providers.slack_revoke_access_response import SlackRevokeAccessResponse

__all__ = ["SlackResource", "AsyncSlackResource"]


class SlackResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SlackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return SlackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SlackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return SlackResourceWithStreamingResponse(self)

    def check_auth(
        self,
        channel_id: str,
        *,
        access_token_object: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SlackCheckAuthResponse:
        """
        Check if a Slack channel is authenticated.

        Args:
          access_token_object: A JSON encoded string containing the access token object reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get(
            f"/v1/providers/slack/{channel_id}/auth_check",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"access_token_object": access_token_object}, slack_check_auth_params.SlackCheckAuthParams
                ),
            ),
            cast_to=SlackCheckAuthResponse,
        )

    def list_channels(
        self,
        channel_id: str,
        *,
        access_token_object: str,
        query_options: slack_list_channels_params.QueryOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSlackChannelsCursor[SlackListChannelsResponse]:
        """
        List Slack channels for a Slack workspace.

        Args:
          access_token_object: A JSON encoded string containing the access token object reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get_api_list(
            f"/v1/providers/slack/{channel_id}/channels",
            page=SyncSlackChannelsCursor[SlackListChannelsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "access_token_object": access_token_object,
                        "query_options": query_options,
                    },
                    slack_list_channels_params.SlackListChannelsParams,
                ),
            ),
            model=SlackListChannelsResponse,
        )

    def revoke_access(
        self,
        channel_id: str,
        *,
        access_token_object: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SlackRevokeAccessResponse:
        """
        Revoke access for a Slack channel.

        Args:
          access_token_object: A JSON encoded string containing the access token object reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._put(
            f"/v1/providers/slack/{channel_id}/revoke_access",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"access_token_object": access_token_object}, slack_revoke_access_params.SlackRevokeAccessParams
                ),
            ),
            cast_to=SlackRevokeAccessResponse,
        )


class AsyncSlackResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSlackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSlackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSlackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncSlackResourceWithStreamingResponse(self)

    async def check_auth(
        self,
        channel_id: str,
        *,
        access_token_object: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SlackCheckAuthResponse:
        """
        Check if a Slack channel is authenticated.

        Args:
          access_token_object: A JSON encoded string containing the access token object reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._get(
            f"/v1/providers/slack/{channel_id}/auth_check",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"access_token_object": access_token_object}, slack_check_auth_params.SlackCheckAuthParams
                ),
            ),
            cast_to=SlackCheckAuthResponse,
        )

    def list_channels(
        self,
        channel_id: str,
        *,
        access_token_object: str,
        query_options: slack_list_channels_params.QueryOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SlackListChannelsResponse, AsyncSlackChannelsCursor[SlackListChannelsResponse]]:
        """
        List Slack channels for a Slack workspace.

        Args:
          access_token_object: A JSON encoded string containing the access token object reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get_api_list(
            f"/v1/providers/slack/{channel_id}/channels",
            page=AsyncSlackChannelsCursor[SlackListChannelsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "access_token_object": access_token_object,
                        "query_options": query_options,
                    },
                    slack_list_channels_params.SlackListChannelsParams,
                ),
            ),
            model=SlackListChannelsResponse,
        )

    async def revoke_access(
        self,
        channel_id: str,
        *,
        access_token_object: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SlackRevokeAccessResponse:
        """
        Revoke access for a Slack channel.

        Args:
          access_token_object: A JSON encoded string containing the access token object reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._put(
            f"/v1/providers/slack/{channel_id}/revoke_access",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"access_token_object": access_token_object}, slack_revoke_access_params.SlackRevokeAccessParams
                ),
            ),
            cast_to=SlackRevokeAccessResponse,
        )


class SlackResourceWithRawResponse:
    def __init__(self, slack: SlackResource) -> None:
        self._slack = slack

        self.check_auth = to_raw_response_wrapper(
            slack.check_auth,
        )
        self.list_channels = to_raw_response_wrapper(
            slack.list_channels,
        )
        self.revoke_access = to_raw_response_wrapper(
            slack.revoke_access,
        )


class AsyncSlackResourceWithRawResponse:
    def __init__(self, slack: AsyncSlackResource) -> None:
        self._slack = slack

        self.check_auth = async_to_raw_response_wrapper(
            slack.check_auth,
        )
        self.list_channels = async_to_raw_response_wrapper(
            slack.list_channels,
        )
        self.revoke_access = async_to_raw_response_wrapper(
            slack.revoke_access,
        )


class SlackResourceWithStreamingResponse:
    def __init__(self, slack: SlackResource) -> None:
        self._slack = slack

        self.check_auth = to_streamed_response_wrapper(
            slack.check_auth,
        )
        self.list_channels = to_streamed_response_wrapper(
            slack.list_channels,
        )
        self.revoke_access = to_streamed_response_wrapper(
            slack.revoke_access,
        )


class AsyncSlackResourceWithStreamingResponse:
    def __init__(self, slack: AsyncSlackResource) -> None:
        self._slack = slack

        self.check_auth = async_to_streamed_response_wrapper(
            slack.check_auth,
        )
        self.list_channels = async_to_streamed_response_wrapper(
            slack.list_channels,
        )
        self.revoke_access = async_to_streamed_response_wrapper(
            slack.revoke_access,
        )
