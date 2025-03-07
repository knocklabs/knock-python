# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime

import httpx

from ..types import (
    schedule_list_params,
    schedule_create_params,
    schedule_delete_params,
    schedule_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncEntriesCursor, AsyncEntriesCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.shared.schedule import Schedule
from ..types.schedule_create_response import ScheduleCreateResponse
from ..types.schedule_delete_response import ScheduleDeleteResponse
from ..types.schedule_update_response import ScheduleUpdateResponse
from ..types.shared_params.recipient_request import RecipientRequest
from ..types.shared_params.schedule_repeat_rule import ScheduleRepeatRule
from ..types.shared_params.inline_tenant_request import InlineTenantRequest

__all__ = ["SchedulesResource", "AsyncSchedulesResource"]


class SchedulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchedulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/knock-python#accessing-raw-response-data-eg-headers
        """
        return SchedulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchedulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/knock-python#with_streaming_response
        """
        return SchedulesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        recipients: List[schedule_create_params.Recipient],
        repeats: Iterable[ScheduleRepeatRule],
        workflow: str,
        data: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        ending_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        scheduled_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        tenant: Optional[InlineTenantRequest] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleCreateResponse:
        """
        Create schedules

        Args:
          tenant: An inline tenant request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/schedules",
            body=maybe_transform(
                {
                    "recipients": recipients,
                    "repeats": repeats,
                    "workflow": workflow,
                    "data": data,
                    "ending_at": ending_at,
                    "scheduled_at": scheduled_at,
                    "tenant": tenant,
                },
                schedule_create_params.ScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleCreateResponse,
        )

    def update(
        self,
        *,
        schedule_ids: List[str],
        actor: Optional[RecipientRequest] | NotGiven = NOT_GIVEN,
        data: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        ending_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        repeats: Iterable[ScheduleRepeatRule] | NotGiven = NOT_GIVEN,
        scheduled_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        tenant: Optional[InlineTenantRequest] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleUpdateResponse:
        """Update schedules

        Args:
          actor: Specifies a recipient in a request.

        This can either be a user identifier
              (string), an inline user request (object), or an inline object request, which is
              determined by the presence of a `collection` property.

          tenant: An inline tenant request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/schedules",
            body=maybe_transform(
                {
                    "schedule_ids": schedule_ids,
                    "actor": actor,
                    "data": data,
                    "ending_at": ending_at,
                    "repeats": repeats,
                    "scheduled_at": scheduled_at,
                    "tenant": tenant,
                },
                schedule_update_params.ScheduleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleUpdateResponse,
        )

    def list(
        self,
        *,
        workflow: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        recipients: List[schedule_list_params.Recipient] | NotGiven = NOT_GIVEN,
        tenant: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncEntriesCursor[Schedule]:
        """
        List schedules

        Args:
          workflow: Filter by workflow

          after: The cursor to fetch entries after

          before: The cursor to fetch entries before

          page_size: The page size to fetch

          recipients: Filter by recipient

          tenant: Filter by tenant

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/schedules",
            page=SyncEntriesCursor[Schedule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "workflow": workflow,
                        "after": after,
                        "before": before,
                        "page_size": page_size,
                        "recipients": recipients,
                        "tenant": tenant,
                    },
                    schedule_list_params.ScheduleListParams,
                ),
            ),
            model=Schedule,
        )

    def delete(
        self,
        *,
        schedule_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleDeleteResponse:
        """
        Delete schedules

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v1/schedules",
            body=maybe_transform({"schedule_ids": schedule_ids}, schedule_delete_params.ScheduleDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleDeleteResponse,
        )


class AsyncSchedulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchedulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchedulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchedulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/knock-python#with_streaming_response
        """
        return AsyncSchedulesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        recipients: List[schedule_create_params.Recipient],
        repeats: Iterable[ScheduleRepeatRule],
        workflow: str,
        data: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        ending_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        scheduled_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        tenant: Optional[InlineTenantRequest] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleCreateResponse:
        """
        Create schedules

        Args:
          tenant: An inline tenant request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/schedules",
            body=await async_maybe_transform(
                {
                    "recipients": recipients,
                    "repeats": repeats,
                    "workflow": workflow,
                    "data": data,
                    "ending_at": ending_at,
                    "scheduled_at": scheduled_at,
                    "tenant": tenant,
                },
                schedule_create_params.ScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleCreateResponse,
        )

    async def update(
        self,
        *,
        schedule_ids: List[str],
        actor: Optional[RecipientRequest] | NotGiven = NOT_GIVEN,
        data: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        ending_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        repeats: Iterable[ScheduleRepeatRule] | NotGiven = NOT_GIVEN,
        scheduled_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        tenant: Optional[InlineTenantRequest] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleUpdateResponse:
        """Update schedules

        Args:
          actor: Specifies a recipient in a request.

        This can either be a user identifier
              (string), an inline user request (object), or an inline object request, which is
              determined by the presence of a `collection` property.

          tenant: An inline tenant request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/schedules",
            body=await async_maybe_transform(
                {
                    "schedule_ids": schedule_ids,
                    "actor": actor,
                    "data": data,
                    "ending_at": ending_at,
                    "repeats": repeats,
                    "scheduled_at": scheduled_at,
                    "tenant": tenant,
                },
                schedule_update_params.ScheduleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleUpdateResponse,
        )

    def list(
        self,
        *,
        workflow: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        recipients: List[schedule_list_params.Recipient] | NotGiven = NOT_GIVEN,
        tenant: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Schedule, AsyncEntriesCursor[Schedule]]:
        """
        List schedules

        Args:
          workflow: Filter by workflow

          after: The cursor to fetch entries after

          before: The cursor to fetch entries before

          page_size: The page size to fetch

          recipients: Filter by recipient

          tenant: Filter by tenant

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/schedules",
            page=AsyncEntriesCursor[Schedule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "workflow": workflow,
                        "after": after,
                        "before": before,
                        "page_size": page_size,
                        "recipients": recipients,
                        "tenant": tenant,
                    },
                    schedule_list_params.ScheduleListParams,
                ),
            ),
            model=Schedule,
        )

    async def delete(
        self,
        *,
        schedule_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleDeleteResponse:
        """
        Delete schedules

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v1/schedules",
            body=await async_maybe_transform(
                {"schedule_ids": schedule_ids}, schedule_delete_params.ScheduleDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleDeleteResponse,
        )


class SchedulesResourceWithRawResponse:
    def __init__(self, schedules: SchedulesResource) -> None:
        self._schedules = schedules

        self.create = to_raw_response_wrapper(
            schedules.create,
        )
        self.update = to_raw_response_wrapper(
            schedules.update,
        )
        self.list = to_raw_response_wrapper(
            schedules.list,
        )
        self.delete = to_raw_response_wrapper(
            schedules.delete,
        )


class AsyncSchedulesResourceWithRawResponse:
    def __init__(self, schedules: AsyncSchedulesResource) -> None:
        self._schedules = schedules

        self.create = async_to_raw_response_wrapper(
            schedules.create,
        )
        self.update = async_to_raw_response_wrapper(
            schedules.update,
        )
        self.list = async_to_raw_response_wrapper(
            schedules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            schedules.delete,
        )


class SchedulesResourceWithStreamingResponse:
    def __init__(self, schedules: SchedulesResource) -> None:
        self._schedules = schedules

        self.create = to_streamed_response_wrapper(
            schedules.create,
        )
        self.update = to_streamed_response_wrapper(
            schedules.update,
        )
        self.list = to_streamed_response_wrapper(
            schedules.list,
        )
        self.delete = to_streamed_response_wrapper(
            schedules.delete,
        )


class AsyncSchedulesResourceWithStreamingResponse:
    def __init__(self, schedules: AsyncSchedulesResource) -> None:
        self._schedules = schedules

        self.create = async_to_streamed_response_wrapper(
            schedules.create,
        )
        self.update = async_to_streamed_response_wrapper(
            schedules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            schedules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            schedules.delete,
        )
