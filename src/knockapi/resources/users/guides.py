# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

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
from ...types.users import (
    guide_get_channel_params,
    guide_mark_message_as_seen_params,
    guide_mark_message_as_archived_params,
    guide_mark_message_as_interacted_params,
)
from ..._base_client import make_request_options
from ...types.users.guide_get_channel_response import GuideGetChannelResponse
from ...types.users.guide_mark_message_as_seen_response import GuideMarkMessageAsSeenResponse
from ...types.users.guide_mark_message_as_archived_response import GuideMarkMessageAsArchivedResponse
from ...types.users.guide_mark_message_as_interacted_response import GuideMarkMessageAsInteractedResponse

__all__ = ["GuidesResource", "AsyncGuidesResource"]


class GuidesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GuidesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return GuidesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GuidesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return GuidesResourceWithStreamingResponse(self)

    def get_channel(
        self,
        user_id: str,
        channel_id: str,
        *,
        data: str | NotGiven = NOT_GIVEN,
        tenant: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuideGetChannelResponse:
        """
        Returns a list of eligible in-app guides for a specific user and channel.

        Args:
          data: The data (JSON encoded object) to use for targeting and rendering guides.

          tenant: The tenant ID to use for targeting and rendering guides.

          type: The type of guides to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return self._get(
            f"/v1/users/{user_id}/guides/{channel_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "data": data,
                        "tenant": tenant,
                        "type": type,
                    },
                    guide_get_channel_params.GuideGetChannelParams,
                ),
            ),
            cast_to=GuideGetChannelResponse,
        )

    def mark_message_as_archived(
        self,
        user_id: str,
        message_id: str,
        *,
        channel_id: str,
        guide_id: str,
        guide_key: str,
        guide_step_ref: str,
        content: Dict[str, object] | NotGiven = NOT_GIVEN,
        data: Dict[str, object] | NotGiven = NOT_GIVEN,
        is_final: bool | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        tenant: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuideMarkMessageAsArchivedResponse:
        """
        Records that a guide has been archived by a user, triggering any associated
        archived events.

        Args:
          channel_id: The unique identifier for the channel.

          guide_id: The unique identifier for the guide.

          guide_key: The key of the guide.

          guide_step_ref: The step reference of the guide.

          content: The content of the guide.

          data: The data of the guide.

          is_final: Whether the guide is final.

          metadata: The metadata of the guide.

          tenant: The tenant ID of the guide.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._put(
            f"/v1/users/{user_id}/guides/messages/{message_id}/archived",
            body=maybe_transform(
                {
                    "channel_id": channel_id,
                    "guide_id": guide_id,
                    "guide_key": guide_key,
                    "guide_step_ref": guide_step_ref,
                    "content": content,
                    "data": data,
                    "is_final": is_final,
                    "metadata": metadata,
                    "tenant": tenant,
                },
                guide_mark_message_as_archived_params.GuideMarkMessageAsArchivedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GuideMarkMessageAsArchivedResponse,
        )

    def mark_message_as_interacted(
        self,
        user_id: str,
        message_id: str,
        *,
        channel_id: str,
        guide_id: str,
        guide_key: str,
        guide_step_ref: str,
        content: Dict[str, object] | NotGiven = NOT_GIVEN,
        data: Dict[str, object] | NotGiven = NOT_GIVEN,
        is_final: bool | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        tenant: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuideMarkMessageAsInteractedResponse:
        """
        Records that a user has interacted with a guide, triggering any associated
        interacted events.

        Args:
          channel_id: The unique identifier for the channel.

          guide_id: The unique identifier for the guide.

          guide_key: The key of the guide.

          guide_step_ref: The step reference of the guide.

          content: The content of the guide.

          data: The data of the guide.

          is_final: Whether the guide is final.

          metadata: The metadata of the guide.

          tenant: The tenant ID of the guide.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._put(
            f"/v1/users/{user_id}/guides/messages/{message_id}/interacted",
            body=maybe_transform(
                {
                    "channel_id": channel_id,
                    "guide_id": guide_id,
                    "guide_key": guide_key,
                    "guide_step_ref": guide_step_ref,
                    "content": content,
                    "data": data,
                    "is_final": is_final,
                    "metadata": metadata,
                    "tenant": tenant,
                },
                guide_mark_message_as_interacted_params.GuideMarkMessageAsInteractedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GuideMarkMessageAsInteractedResponse,
        )

    def mark_message_as_seen(
        self,
        user_id: str,
        message_id: str,
        *,
        channel_id: str,
        guide_id: str,
        guide_key: str,
        guide_step_ref: str,
        content: Dict[str, object] | NotGiven = NOT_GIVEN,
        data: Dict[str, object] | NotGiven = NOT_GIVEN,
        is_final: bool | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        tenant: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuideMarkMessageAsSeenResponse:
        """
        Records that a guide has been seen by a user, triggering any associated seen
        events.

        Args:
          channel_id: The unique identifier for the channel.

          guide_id: The unique identifier for the guide.

          guide_key: The key of the guide.

          guide_step_ref: The step reference of the guide.

          content: The content of the guide.

          data: The data of the guide.

          is_final: Whether the guide is final.

          metadata: The metadata of the guide.

          tenant: The tenant ID of the guide.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._put(
            f"/v1/users/{user_id}/guides/messages/{message_id}/seen",
            body=maybe_transform(
                {
                    "channel_id": channel_id,
                    "guide_id": guide_id,
                    "guide_key": guide_key,
                    "guide_step_ref": guide_step_ref,
                    "content": content,
                    "data": data,
                    "is_final": is_final,
                    "metadata": metadata,
                    "tenant": tenant,
                },
                guide_mark_message_as_seen_params.GuideMarkMessageAsSeenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GuideMarkMessageAsSeenResponse,
        )


class AsyncGuidesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGuidesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGuidesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGuidesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncGuidesResourceWithStreamingResponse(self)

    async def get_channel(
        self,
        user_id: str,
        channel_id: str,
        *,
        data: str | NotGiven = NOT_GIVEN,
        tenant: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuideGetChannelResponse:
        """
        Returns a list of eligible in-app guides for a specific user and channel.

        Args:
          data: The data (JSON encoded object) to use for targeting and rendering guides.

          tenant: The tenant ID to use for targeting and rendering guides.

          type: The type of guides to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not channel_id:
            raise ValueError(f"Expected a non-empty value for `channel_id` but received {channel_id!r}")
        return await self._get(
            f"/v1/users/{user_id}/guides/{channel_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "data": data,
                        "tenant": tenant,
                        "type": type,
                    },
                    guide_get_channel_params.GuideGetChannelParams,
                ),
            ),
            cast_to=GuideGetChannelResponse,
        )

    async def mark_message_as_archived(
        self,
        user_id: str,
        message_id: str,
        *,
        channel_id: str,
        guide_id: str,
        guide_key: str,
        guide_step_ref: str,
        content: Dict[str, object] | NotGiven = NOT_GIVEN,
        data: Dict[str, object] | NotGiven = NOT_GIVEN,
        is_final: bool | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        tenant: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuideMarkMessageAsArchivedResponse:
        """
        Records that a guide has been archived by a user, triggering any associated
        archived events.

        Args:
          channel_id: The unique identifier for the channel.

          guide_id: The unique identifier for the guide.

          guide_key: The key of the guide.

          guide_step_ref: The step reference of the guide.

          content: The content of the guide.

          data: The data of the guide.

          is_final: Whether the guide is final.

          metadata: The metadata of the guide.

          tenant: The tenant ID of the guide.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._put(
            f"/v1/users/{user_id}/guides/messages/{message_id}/archived",
            body=await async_maybe_transform(
                {
                    "channel_id": channel_id,
                    "guide_id": guide_id,
                    "guide_key": guide_key,
                    "guide_step_ref": guide_step_ref,
                    "content": content,
                    "data": data,
                    "is_final": is_final,
                    "metadata": metadata,
                    "tenant": tenant,
                },
                guide_mark_message_as_archived_params.GuideMarkMessageAsArchivedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GuideMarkMessageAsArchivedResponse,
        )

    async def mark_message_as_interacted(
        self,
        user_id: str,
        message_id: str,
        *,
        channel_id: str,
        guide_id: str,
        guide_key: str,
        guide_step_ref: str,
        content: Dict[str, object] | NotGiven = NOT_GIVEN,
        data: Dict[str, object] | NotGiven = NOT_GIVEN,
        is_final: bool | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        tenant: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuideMarkMessageAsInteractedResponse:
        """
        Records that a user has interacted with a guide, triggering any associated
        interacted events.

        Args:
          channel_id: The unique identifier for the channel.

          guide_id: The unique identifier for the guide.

          guide_key: The key of the guide.

          guide_step_ref: The step reference of the guide.

          content: The content of the guide.

          data: The data of the guide.

          is_final: Whether the guide is final.

          metadata: The metadata of the guide.

          tenant: The tenant ID of the guide.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._put(
            f"/v1/users/{user_id}/guides/messages/{message_id}/interacted",
            body=await async_maybe_transform(
                {
                    "channel_id": channel_id,
                    "guide_id": guide_id,
                    "guide_key": guide_key,
                    "guide_step_ref": guide_step_ref,
                    "content": content,
                    "data": data,
                    "is_final": is_final,
                    "metadata": metadata,
                    "tenant": tenant,
                },
                guide_mark_message_as_interacted_params.GuideMarkMessageAsInteractedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GuideMarkMessageAsInteractedResponse,
        )

    async def mark_message_as_seen(
        self,
        user_id: str,
        message_id: str,
        *,
        channel_id: str,
        guide_id: str,
        guide_key: str,
        guide_step_ref: str,
        content: Dict[str, object] | NotGiven = NOT_GIVEN,
        data: Dict[str, object] | NotGiven = NOT_GIVEN,
        is_final: bool | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        tenant: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuideMarkMessageAsSeenResponse:
        """
        Records that a guide has been seen by a user, triggering any associated seen
        events.

        Args:
          channel_id: The unique identifier for the channel.

          guide_id: The unique identifier for the guide.

          guide_key: The key of the guide.

          guide_step_ref: The step reference of the guide.

          content: The content of the guide.

          data: The data of the guide.

          is_final: Whether the guide is final.

          metadata: The metadata of the guide.

          tenant: The tenant ID of the guide.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._put(
            f"/v1/users/{user_id}/guides/messages/{message_id}/seen",
            body=await async_maybe_transform(
                {
                    "channel_id": channel_id,
                    "guide_id": guide_id,
                    "guide_key": guide_key,
                    "guide_step_ref": guide_step_ref,
                    "content": content,
                    "data": data,
                    "is_final": is_final,
                    "metadata": metadata,
                    "tenant": tenant,
                },
                guide_mark_message_as_seen_params.GuideMarkMessageAsSeenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GuideMarkMessageAsSeenResponse,
        )


class GuidesResourceWithRawResponse:
    def __init__(self, guides: GuidesResource) -> None:
        self._guides = guides

        self.get_channel = to_raw_response_wrapper(
            guides.get_channel,
        )
        self.mark_message_as_archived = to_raw_response_wrapper(
            guides.mark_message_as_archived,
        )
        self.mark_message_as_interacted = to_raw_response_wrapper(
            guides.mark_message_as_interacted,
        )
        self.mark_message_as_seen = to_raw_response_wrapper(
            guides.mark_message_as_seen,
        )


class AsyncGuidesResourceWithRawResponse:
    def __init__(self, guides: AsyncGuidesResource) -> None:
        self._guides = guides

        self.get_channel = async_to_raw_response_wrapper(
            guides.get_channel,
        )
        self.mark_message_as_archived = async_to_raw_response_wrapper(
            guides.mark_message_as_archived,
        )
        self.mark_message_as_interacted = async_to_raw_response_wrapper(
            guides.mark_message_as_interacted,
        )
        self.mark_message_as_seen = async_to_raw_response_wrapper(
            guides.mark_message_as_seen,
        )


class GuidesResourceWithStreamingResponse:
    def __init__(self, guides: GuidesResource) -> None:
        self._guides = guides

        self.get_channel = to_streamed_response_wrapper(
            guides.get_channel,
        )
        self.mark_message_as_archived = to_streamed_response_wrapper(
            guides.mark_message_as_archived,
        )
        self.mark_message_as_interacted = to_streamed_response_wrapper(
            guides.mark_message_as_interacted,
        )
        self.mark_message_as_seen = to_streamed_response_wrapper(
            guides.mark_message_as_seen,
        )


class AsyncGuidesResourceWithStreamingResponse:
    def __init__(self, guides: AsyncGuidesResource) -> None:
        self._guides = guides

        self.get_channel = async_to_streamed_response_wrapper(
            guides.get_channel,
        )
        self.mark_message_as_archived = async_to_streamed_response_wrapper(
            guides.mark_message_as_archived,
        )
        self.mark_message_as_interacted = async_to_streamed_response_wrapper(
            guides.mark_message_as_interacted,
        )
        self.mark_message_as_seen = async_to_streamed_response_wrapper(
            guides.mark_message_as_seen,
        )
