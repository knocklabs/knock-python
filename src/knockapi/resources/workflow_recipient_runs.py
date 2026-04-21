# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import workflow_recipient_run_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncItemsCursor, AsyncItemsCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.workflow_recipient_run import WorkflowRecipientRun
from ..types.recipient_reference_param import RecipientReferenceParam
from ..types.workflow_recipient_run_detail import WorkflowRecipientRunDetail

__all__ = ["WorkflowRecipientRunsResource", "AsyncWorkflowRecipientRunsResource"]


class WorkflowRecipientRunsResource(SyncAPIResource):
    """
    A workflow run represents an individual execution of a workflow for a specific recipient.
    """

    @cached_property
    def with_raw_response(self) -> WorkflowRecipientRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return WorkflowRecipientRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkflowRecipientRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return WorkflowRecipientRunsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        ending_at: Union[str, datetime] | Omit = omit,
        has_errors: bool | Omit = omit,
        page_size: int | Omit = omit,
        recipient: RecipientReferenceParam | Omit = omit,
        starting_at: Union[str, datetime] | Omit = omit,
        status: List[Literal["queued", "processing", "paused", "completed", "cancelled"]] | Omit = omit,
        tenant: str | Omit = omit,
        workflow: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncItemsCursor[WorkflowRecipientRun]:
        """
        Returns a paginated list of workflow recipient runs for the current environment.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          ending_at: Limits the results to workflow recipient runs started before the given date.

          has_errors: Limits the results to workflow recipient runs that have errors.

          page_size: The number of items per page (defaults to 50).

          recipient: Limits the results to workflow recipient runs for the given recipient. Accepts a
              user ID string or an object reference with `id` and `collection`.

          starting_at: Limits the results to workflow recipient runs started after the given date.

          status: Limits the results to workflow recipient runs with the given status.

          tenant: Limits the results to workflow recipient runs for the given tenant.

          workflow: Limits the results to workflow recipient runs for the given workflow key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/workflow_recipient_runs",
            page=SyncItemsCursor[WorkflowRecipientRun],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "ending_at": ending_at,
                        "has_errors": has_errors,
                        "page_size": page_size,
                        "recipient": recipient,
                        "starting_at": starting_at,
                        "status": status,
                        "tenant": tenant,
                        "workflow": workflow,
                    },
                    workflow_recipient_run_list_params.WorkflowRecipientRunListParams,
                ),
            ),
            model=WorkflowRecipientRun,
        )

    def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowRecipientRunDetail:
        """
        Returns a single workflow recipient run with its associated events.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/workflow_recipient_runs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowRecipientRunDetail,
        )


class AsyncWorkflowRecipientRunsResource(AsyncAPIResource):
    """
    A workflow run represents an individual execution of a workflow for a specific recipient.
    """

    @cached_property
    def with_raw_response(self) -> AsyncWorkflowRecipientRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkflowRecipientRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkflowRecipientRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncWorkflowRecipientRunsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        ending_at: Union[str, datetime] | Omit = omit,
        has_errors: bool | Omit = omit,
        page_size: int | Omit = omit,
        recipient: RecipientReferenceParam | Omit = omit,
        starting_at: Union[str, datetime] | Omit = omit,
        status: List[Literal["queued", "processing", "paused", "completed", "cancelled"]] | Omit = omit,
        tenant: str | Omit = omit,
        workflow: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WorkflowRecipientRun, AsyncItemsCursor[WorkflowRecipientRun]]:
        """
        Returns a paginated list of workflow recipient runs for the current environment.

        Args:
          after: The cursor to fetch entries after.

          before: The cursor to fetch entries before.

          ending_at: Limits the results to workflow recipient runs started before the given date.

          has_errors: Limits the results to workflow recipient runs that have errors.

          page_size: The number of items per page (defaults to 50).

          recipient: Limits the results to workflow recipient runs for the given recipient. Accepts a
              user ID string or an object reference with `id` and `collection`.

          starting_at: Limits the results to workflow recipient runs started after the given date.

          status: Limits the results to workflow recipient runs with the given status.

          tenant: Limits the results to workflow recipient runs for the given tenant.

          workflow: Limits the results to workflow recipient runs for the given workflow key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/workflow_recipient_runs",
            page=AsyncItemsCursor[WorkflowRecipientRun],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "ending_at": ending_at,
                        "has_errors": has_errors,
                        "page_size": page_size,
                        "recipient": recipient,
                        "starting_at": starting_at,
                        "status": status,
                        "tenant": tenant,
                        "workflow": workflow,
                    },
                    workflow_recipient_run_list_params.WorkflowRecipientRunListParams,
                ),
            ),
            model=WorkflowRecipientRun,
        )

    async def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowRecipientRunDetail:
        """
        Returns a single workflow recipient run with its associated events.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/workflow_recipient_runs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowRecipientRunDetail,
        )


class WorkflowRecipientRunsResourceWithRawResponse:
    def __init__(self, workflow_recipient_runs: WorkflowRecipientRunsResource) -> None:
        self._workflow_recipient_runs = workflow_recipient_runs

        self.list = to_raw_response_wrapper(
            workflow_recipient_runs.list,
        )
        self.get = to_raw_response_wrapper(
            workflow_recipient_runs.get,
        )


class AsyncWorkflowRecipientRunsResourceWithRawResponse:
    def __init__(self, workflow_recipient_runs: AsyncWorkflowRecipientRunsResource) -> None:
        self._workflow_recipient_runs = workflow_recipient_runs

        self.list = async_to_raw_response_wrapper(
            workflow_recipient_runs.list,
        )
        self.get = async_to_raw_response_wrapper(
            workflow_recipient_runs.get,
        )


class WorkflowRecipientRunsResourceWithStreamingResponse:
    def __init__(self, workflow_recipient_runs: WorkflowRecipientRunsResource) -> None:
        self._workflow_recipient_runs = workflow_recipient_runs

        self.list = to_streamed_response_wrapper(
            workflow_recipient_runs.list,
        )
        self.get = to_streamed_response_wrapper(
            workflow_recipient_runs.get,
        )


class AsyncWorkflowRecipientRunsResourceWithStreamingResponse:
    def __init__(self, workflow_recipient_runs: AsyncWorkflowRecipientRunsResource) -> None:
        self._workflow_recipient_runs = workflow_recipient_runs

        self.list = async_to_streamed_response_wrapper(
            workflow_recipient_runs.list,
        )
        self.get = async_to_streamed_response_wrapper(
            workflow_recipient_runs.get,
        )
