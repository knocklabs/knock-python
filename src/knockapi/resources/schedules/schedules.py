# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime

import httpx

from .bulk import (
    BulkResource,
    AsyncBulkResource,
    BulkResourceWithRawResponse,
    AsyncBulkResourceWithRawResponse,
    BulkResourceWithStreamingResponse,
    AsyncBulkResourceWithStreamingResponse,
)
from ...types import (
    schedule_list_params,
    schedule_create_params,
    schedule_delete_params,
    schedule_update_params,
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
from ...pagination import SyncEntriesCursor, AsyncEntriesCursor
from ..._base_client import AsyncPaginator, make_request_options
from ...types.schedule import Schedule
from ...types.recipient_request_param import RecipientRequestParam
from ...types.schedule_create_response import ScheduleCreateResponse
from ...types.schedule_delete_response import ScheduleDeleteResponse
from ...types.schedule_update_response import ScheduleUpdateResponse
from ...types.recipient_reference_param import RecipientReferenceParam
from ...types.schedule_repeat_rule_param import ScheduleRepeatRuleParam
from ...types.inline_tenant_request_param import InlineTenantRequestParam

__all__ = ["SchedulesResource", "AsyncSchedulesResource"]


class SchedulesResource(SyncAPIResource):
    @cached_property
    def bulk(self) -> BulkResource:
        return BulkResource(self._client)

    @cached_property
    def with_raw_response(self) -> SchedulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return SchedulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchedulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return SchedulesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        recipients: List[RecipientRequestParam],
        workflow: str,
        actor: Optional[RecipientRequestParam] | NotGiven = NOT_GIVEN,
        data: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        ending_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        repeats: Iterable[ScheduleRepeatRuleParam] | NotGiven = NOT_GIVEN,
        scheduled_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        tenant: Optional[InlineTenantRequestParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleCreateResponse:
        """
        Creates one or more schedules for a workflow with the specified recipients,
        timing, and data. Schedules can be one-time or recurring. This endpoint also
        handles
        [inline identifications](/managing-recipients/identifying-recipients#inline-identifying-recipients)
        for the `actor`, `recipient`, and `tenant` fields.

        Args:
          recipients: The recipients to set the schedule for. Limited to 100 recipients per request.

          workflow: The key of the workflow.

          actor: Specifies a recipient in a request. This can either be a user identifier
              (string), an inline user request (object), or an inline object request, which is
              determined by the presence of a `collection` property.

          data: An optional map of data to pass into the workflow execution. There is a 1024
              byte limit on the size of any single string value (with the exception of
              [email attachments](/integrations/email/attachments)), and a 10MB limit on the
              size of the full `data` payload.

          ending_at: The ending date and time for the schedule.

          repeats: The repeat rule for the schedule.

          scheduled_at: The starting date and time for the schedule.

          tenant: An request to set a tenant inline.

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
                    "workflow": workflow,
                    "actor": actor,
                    "data": data,
                    "ending_at": ending_at,
                    "repeats": repeats,
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
        actor: Optional[RecipientReferenceParam] | NotGiven = NOT_GIVEN,
        data: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        ending_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        repeats: Iterable[ScheduleRepeatRuleParam] | NotGiven = NOT_GIVEN,
        scheduled_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        tenant: Optional[InlineTenantRequestParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleUpdateResponse:
        """
        Updates one or more existing schedules with new timing, data, or other
        properties. All specified schedule IDs will be updated with the same values.
        This endpoint also handles
        [inline identifications](/managing-recipients/identifying-recipients#inline-identifying-recipients)
        for the `actor`, `recipient`, and `tenant` fields.

        Args:
          schedule_ids: A list of schedule IDs.

          actor: A reference to a recipient, either a user identifier (string) or an object
              reference (ID, collection).

          data: An optional map of data to pass into the workflow execution. There is a 1024
              byte limit on the size of any single string value (with the exception of
              [email attachments](/integrations/email/attachments)), and a 10MB limit on the
              size of the full `data` payload.

          ending_at: The ending date and time for the schedule.

          repeats: The repeat rule for the schedule.

          scheduled_at: The starting date and time for the schedule.

          tenant: An request to set a tenant inline.

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
        recipients: List[RecipientReferenceParam] | NotGiven = NOT_GIVEN,
        tenant: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncEntriesCursor[Schedule]:
        """
        Returns a paginated list of schedules for the current environment, filtered by
        workflow and optionally by recipients and tenant.

        Args:
          workflow: Filter by workflow key.

          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          page_size: The number of items per page.

          recipients: Filter by recipient references.

          tenant: Filter by tenant ID.

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
        Permanently deletes one or more schedules identified by the provided schedule
        IDs. This operation cannot be undone.

        Args:
          schedule_ids: A list of schedule IDs.

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
    def bulk(self) -> AsyncBulkResource:
        return AsyncBulkResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSchedulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchedulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchedulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncSchedulesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        recipients: List[RecipientRequestParam],
        workflow: str,
        actor: Optional[RecipientRequestParam] | NotGiven = NOT_GIVEN,
        data: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        ending_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        repeats: Iterable[ScheduleRepeatRuleParam] | NotGiven = NOT_GIVEN,
        scheduled_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        tenant: Optional[InlineTenantRequestParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleCreateResponse:
        """
        Creates one or more schedules for a workflow with the specified recipients,
        timing, and data. Schedules can be one-time or recurring. This endpoint also
        handles
        [inline identifications](/managing-recipients/identifying-recipients#inline-identifying-recipients)
        for the `actor`, `recipient`, and `tenant` fields.

        Args:
          recipients: The recipients to set the schedule for. Limited to 100 recipients per request.

          workflow: The key of the workflow.

          actor: Specifies a recipient in a request. This can either be a user identifier
              (string), an inline user request (object), or an inline object request, which is
              determined by the presence of a `collection` property.

          data: An optional map of data to pass into the workflow execution. There is a 1024
              byte limit on the size of any single string value (with the exception of
              [email attachments](/integrations/email/attachments)), and a 10MB limit on the
              size of the full `data` payload.

          ending_at: The ending date and time for the schedule.

          repeats: The repeat rule for the schedule.

          scheduled_at: The starting date and time for the schedule.

          tenant: An request to set a tenant inline.

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
                    "workflow": workflow,
                    "actor": actor,
                    "data": data,
                    "ending_at": ending_at,
                    "repeats": repeats,
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
        actor: Optional[RecipientReferenceParam] | NotGiven = NOT_GIVEN,
        data: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        ending_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        repeats: Iterable[ScheduleRepeatRuleParam] | NotGiven = NOT_GIVEN,
        scheduled_at: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        tenant: Optional[InlineTenantRequestParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleUpdateResponse:
        """
        Updates one or more existing schedules with new timing, data, or other
        properties. All specified schedule IDs will be updated with the same values.
        This endpoint also handles
        [inline identifications](/managing-recipients/identifying-recipients#inline-identifying-recipients)
        for the `actor`, `recipient`, and `tenant` fields.

        Args:
          schedule_ids: A list of schedule IDs.

          actor: A reference to a recipient, either a user identifier (string) or an object
              reference (ID, collection).

          data: An optional map of data to pass into the workflow execution. There is a 1024
              byte limit on the size of any single string value (with the exception of
              [email attachments](/integrations/email/attachments)), and a 10MB limit on the
              size of the full `data` payload.

          ending_at: The ending date and time for the schedule.

          repeats: The repeat rule for the schedule.

          scheduled_at: The starting date and time for the schedule.

          tenant: An request to set a tenant inline.

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
        recipients: List[RecipientReferenceParam] | NotGiven = NOT_GIVEN,
        tenant: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Schedule, AsyncEntriesCursor[Schedule]]:
        """
        Returns a paginated list of schedules for the current environment, filtered by
        workflow and optionally by recipients and tenant.

        Args:
          workflow: Filter by workflow key.

          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          page_size: The number of items per page.

          recipients: Filter by recipient references.

          tenant: Filter by tenant ID.

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
        Permanently deletes one or more schedules identified by the provided schedule
        IDs. This operation cannot be undone.

        Args:
          schedule_ids: A list of schedule IDs.

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

    @cached_property
    def bulk(self) -> BulkResourceWithRawResponse:
        return BulkResourceWithRawResponse(self._schedules.bulk)


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

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithRawResponse:
        return AsyncBulkResourceWithRawResponse(self._schedules.bulk)


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

    @cached_property
    def bulk(self) -> BulkResourceWithStreamingResponse:
        return BulkResourceWithStreamingResponse(self._schedules.bulk)


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

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithStreamingResponse:
        return AsyncBulkResourceWithStreamingResponse(self._schedules.bulk)
