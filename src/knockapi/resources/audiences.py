# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import audience_add_members_params, audience_remove_members_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.audience_list_members_response import AudienceListMembersResponse

__all__ = ["AudiencesResource", "AsyncAudiencesResource"]


class AudiencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AudiencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AudiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AudiencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AudiencesResourceWithStreamingResponse(self)

    def add_members(
        self,
        key: str,
        *,
        members: Iterable[audience_add_members_params.Member],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Adds one or more members to the specified audience.

        Args:
          members: A list of audience members to add.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._post(
            f"/v1/audiences/{key}/members",
            body=maybe_transform({"members": members}, audience_add_members_params.AudienceAddMembersParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def list_members(
        self,
        key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AudienceListMembersResponse:
        """
        Returns a paginated list of members for the specified audience.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._get(
            f"/v1/audiences/{key}/members",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AudienceListMembersResponse,
        )

    def remove_members(
        self,
        key: str,
        *,
        members: Iterable[audience_remove_members_params.Member],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Removes one or more members from the specified audience.

        Args:
          members: A list of audience members to remove.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._delete(
            f"/v1/audiences/{key}/members",
            body=maybe_transform({"members": members}, audience_remove_members_params.AudienceRemoveMembersParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncAudiencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAudiencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAudiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAudiencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncAudiencesResourceWithStreamingResponse(self)

    async def add_members(
        self,
        key: str,
        *,
        members: Iterable[audience_add_members_params.Member],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Adds one or more members to the specified audience.

        Args:
          members: A list of audience members to add.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._post(
            f"/v1/audiences/{key}/members",
            body=await async_maybe_transform(
                {"members": members}, audience_add_members_params.AudienceAddMembersParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def list_members(
        self,
        key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AudienceListMembersResponse:
        """
        Returns a paginated list of members for the specified audience.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._get(
            f"/v1/audiences/{key}/members",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AudienceListMembersResponse,
        )

    async def remove_members(
        self,
        key: str,
        *,
        members: Iterable[audience_remove_members_params.Member],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Removes one or more members from the specified audience.

        Args:
          members: A list of audience members to remove.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._delete(
            f"/v1/audiences/{key}/members",
            body=await async_maybe_transform(
                {"members": members}, audience_remove_members_params.AudienceRemoveMembersParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AudiencesResourceWithRawResponse:
    def __init__(self, audiences: AudiencesResource) -> None:
        self._audiences = audiences

        self.add_members = to_raw_response_wrapper(
            audiences.add_members,
        )
        self.list_members = to_raw_response_wrapper(
            audiences.list_members,
        )
        self.remove_members = to_raw_response_wrapper(
            audiences.remove_members,
        )


class AsyncAudiencesResourceWithRawResponse:
    def __init__(self, audiences: AsyncAudiencesResource) -> None:
        self._audiences = audiences

        self.add_members = async_to_raw_response_wrapper(
            audiences.add_members,
        )
        self.list_members = async_to_raw_response_wrapper(
            audiences.list_members,
        )
        self.remove_members = async_to_raw_response_wrapper(
            audiences.remove_members,
        )


class AudiencesResourceWithStreamingResponse:
    def __init__(self, audiences: AudiencesResource) -> None:
        self._audiences = audiences

        self.add_members = to_streamed_response_wrapper(
            audiences.add_members,
        )
        self.list_members = to_streamed_response_wrapper(
            audiences.list_members,
        )
        self.remove_members = to_streamed_response_wrapper(
            audiences.remove_members,
        )


class AsyncAudiencesResourceWithStreamingResponse:
    def __init__(self, audiences: AsyncAudiencesResource) -> None:
        self._audiences = audiences

        self.add_members = async_to_streamed_response_wrapper(
            audiences.add_members,
        )
        self.list_members = async_to_streamed_response_wrapper(
            audiences.list_members,
        )
        self.remove_members = async_to_streamed_response_wrapper(
            audiences.remove_members,
        )
