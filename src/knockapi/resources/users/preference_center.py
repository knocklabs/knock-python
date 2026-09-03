# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.users.preference_center_get_config_response import PreferenceCenterGetConfigResponse
from ...types.users.preference_center_generate_signed_url_response import PreferenceCenterGenerateSignedURLResponse

__all__ = ["PreferenceCenterResource", "AsyncPreferenceCenterResource"]


class PreferenceCenterResource(SyncAPIResource):
    """
    The preference center is a hosted page where users can manage their notification preferences.
    """

    @cached_property
    def with_raw_response(self) -> PreferenceCenterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return PreferenceCenterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreferenceCenterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return PreferenceCenterResourceWithStreamingResponse(self)

    def generate_signed_url(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PreferenceCenterGenerateSignedURLResponse:
        """
        Generates a signed preference center URL and token for the given user in the
        current environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._post(
            path_template("/v1/users/{user_id}/preference_center/signed_url", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PreferenceCenterGenerateSignedURLResponse,
        )

    def get_config(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceCenterGetConfigResponse:
        """
        Returns the preference center config with environment metadata for the given
        user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/v1/users/{user_id}/preference_center/config", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceCenterGetConfigResponse,
        )


class AsyncPreferenceCenterResource(AsyncAPIResource):
    """
    The preference center is a hosted page where users can manage their notification preferences.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPreferenceCenterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreferenceCenterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreferenceCenterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncPreferenceCenterResourceWithStreamingResponse(self)

    async def generate_signed_url(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PreferenceCenterGenerateSignedURLResponse:
        """
        Generates a signed preference center URL and token for the given user in the
        current environment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._post(
            path_template("/v1/users/{user_id}/preference_center/signed_url", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PreferenceCenterGenerateSignedURLResponse,
        )

    async def get_config(
        self,
        user_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceCenterGetConfigResponse:
        """
        Returns the preference center config with environment metadata for the given
        user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/v1/users/{user_id}/preference_center/config", user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceCenterGetConfigResponse,
        )


class PreferenceCenterResourceWithRawResponse:
    def __init__(self, preference_center: PreferenceCenterResource) -> None:
        self._preference_center = preference_center

        self.generate_signed_url = to_raw_response_wrapper(
            preference_center.generate_signed_url,
        )
        self.get_config = to_raw_response_wrapper(
            preference_center.get_config,
        )


class AsyncPreferenceCenterResourceWithRawResponse:
    def __init__(self, preference_center: AsyncPreferenceCenterResource) -> None:
        self._preference_center = preference_center

        self.generate_signed_url = async_to_raw_response_wrapper(
            preference_center.generate_signed_url,
        )
        self.get_config = async_to_raw_response_wrapper(
            preference_center.get_config,
        )


class PreferenceCenterResourceWithStreamingResponse:
    def __init__(self, preference_center: PreferenceCenterResource) -> None:
        self._preference_center = preference_center

        self.generate_signed_url = to_streamed_response_wrapper(
            preference_center.generate_signed_url,
        )
        self.get_config = to_streamed_response_wrapper(
            preference_center.get_config,
        )


class AsyncPreferenceCenterResourceWithStreamingResponse:
    def __init__(self, preference_center: AsyncPreferenceCenterResource) -> None:
        self._preference_center = preference_center

        self.generate_signed_url = async_to_streamed_response_wrapper(
            preference_center.generate_signed_url,
        )
        self.get_config = async_to_streamed_response_wrapper(
            preference_center.get_config,
        )
