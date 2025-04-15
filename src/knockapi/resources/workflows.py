# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

import httpx

from ..types import (
    workflow_cancel_params,
    workflow_trigger_params,
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
from .._base_client import make_request_options
from ..types.recipient_request_param import RecipientRequestParam
from ..types.workflow_trigger_response import WorkflowTriggerResponse
from ..types.inline_tenant_request_param import InlineTenantRequestParam

__all__ = ["WorkflowsResource", "AsyncWorkflowsResource"]


class WorkflowsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/knock-python#accessing-raw-response-data-eg-headers
        """
        return WorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/knock-python#with_streaming_response
        """
        return WorkflowsResourceWithStreamingResponse(self)

    def cancel(
        self,
        key: str,
        *,
        cancellation_key: str,
        recipients: Optional[List[str]] | NotGiven = NOT_GIVEN,
        tenant: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Issues a cancellation request to inflight workflow runs

        Args:
          cancellation_key: The cancellation key supplied to the workflow trigger endpoint to use for
              cancelling one or more workflow runs.

          recipients: An optional list of recipients to cancel the workflow for using the cancellation
              key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._post(
            f"/v1/workflows/{key}/cancel",
            body=maybe_transform(
                {
                    "cancellation_key": cancellation_key,
                    "recipients": recipients,
                    "tenant": tenant,
                },
                workflow_cancel_params.WorkflowCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def trigger(
        self,
        key: str,
        *,
        actor: Optional[RecipientRequestParam] | NotGiven = NOT_GIVEN,
        cancellation_key: Optional[str] | NotGiven = NOT_GIVEN,
        data: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        recipients: List[RecipientRequestParam] | NotGiven = NOT_GIVEN,
        tenant: Optional[InlineTenantRequestParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowTriggerResponse:
        """Triggers a workflow

        Args:
          actor: Specifies a recipient in a request.

        This can either be a user identifier
              (string), an inline user request (object), or an inline object request, which is
              determined by the presence of a `collection` property.

          cancellation_key: An optional key that is used in the workflow cancellation endpoint to target a
              cancellation of any workflow runs associated with this trigger.

          data: An optional map of data to be used in the workflow. This data will be available
              to the workflow as a map in the `data` field.

          recipients: The recipients to trigger the workflow for.

          tenant: An inline tenant request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._post(
            f"/v1/workflows/{key}/trigger",
            body=maybe_transform(
                {
                    "actor": actor,
                    "cancellation_key": cancellation_key,
                    "data": data,
                    "recipients": recipients,
                    "tenant": tenant,
                },
                workflow_trigger_params.WorkflowTriggerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowTriggerResponse,
        )


class AsyncWorkflowsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/knock-python#with_streaming_response
        """
        return AsyncWorkflowsResourceWithStreamingResponse(self)

    async def cancel(
        self,
        key: str,
        *,
        cancellation_key: str,
        recipients: Optional[List[str]] | NotGiven = NOT_GIVEN,
        tenant: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Issues a cancellation request to inflight workflow runs

        Args:
          cancellation_key: The cancellation key supplied to the workflow trigger endpoint to use for
              cancelling one or more workflow runs.

          recipients: An optional list of recipients to cancel the workflow for using the cancellation
              key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._post(
            f"/v1/workflows/{key}/cancel",
            body=await async_maybe_transform(
                {
                    "cancellation_key": cancellation_key,
                    "recipients": recipients,
                    "tenant": tenant,
                },
                workflow_cancel_params.WorkflowCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def trigger(
        self,
        key: str,
        *,
        actor: Optional[RecipientRequestParam] | NotGiven = NOT_GIVEN,
        cancellation_key: Optional[str] | NotGiven = NOT_GIVEN,
        data: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        recipients: List[RecipientRequestParam] | NotGiven = NOT_GIVEN,
        tenant: Optional[InlineTenantRequestParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowTriggerResponse:
        """Triggers a workflow

        Args:
          actor: Specifies a recipient in a request.

        This can either be a user identifier
              (string), an inline user request (object), or an inline object request, which is
              determined by the presence of a `collection` property.

          cancellation_key: An optional key that is used in the workflow cancellation endpoint to target a
              cancellation of any workflow runs associated with this trigger.

          data: An optional map of data to be used in the workflow. This data will be available
              to the workflow as a map in the `data` field.

          recipients: The recipients to trigger the workflow for.

          tenant: An inline tenant request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._post(
            f"/v1/workflows/{key}/trigger",
            body=await async_maybe_transform(
                {
                    "actor": actor,
                    "cancellation_key": cancellation_key,
                    "data": data,
                    "recipients": recipients,
                    "tenant": tenant,
                },
                workflow_trigger_params.WorkflowTriggerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkflowTriggerResponse,
        )


class WorkflowsResourceWithRawResponse:
    def __init__(self, workflows: WorkflowsResource) -> None:
        self._workflows = workflows

        self.cancel = to_raw_response_wrapper(
            workflows.cancel,
        )
        self.trigger = to_raw_response_wrapper(
            workflows.trigger,
        )


class AsyncWorkflowsResourceWithRawResponse:
    def __init__(self, workflows: AsyncWorkflowsResource) -> None:
        self._workflows = workflows

        self.cancel = async_to_raw_response_wrapper(
            workflows.cancel,
        )
        self.trigger = async_to_raw_response_wrapper(
            workflows.trigger,
        )


class WorkflowsResourceWithStreamingResponse:
    def __init__(self, workflows: WorkflowsResource) -> None:
        self._workflows = workflows

        self.cancel = to_streamed_response_wrapper(
            workflows.cancel,
        )
        self.trigger = to_streamed_response_wrapper(
            workflows.trigger,
        )


class AsyncWorkflowsResourceWithStreamingResponse:
    def __init__(self, workflows: AsyncWorkflowsResource) -> None:
        self._workflows = workflows

        self.cancel = async_to_streamed_response_wrapper(
            workflows.cancel,
        )
        self.trigger = async_to_streamed_response_wrapper(
            workflows.trigger,
        )
