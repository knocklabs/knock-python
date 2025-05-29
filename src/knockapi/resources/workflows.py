# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

import httpx

from ..types import workflow_cancel_params, workflow_trigger_params
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
from ..types.recipient_request_param import RecipientRequestParam
from ..types.recipient_reference_param import RecipientReferenceParam
from ..types.workflow_trigger_response import WorkflowTriggerResponse
from ..types.inline_tenant_request_param import InlineTenantRequestParam

__all__ = ["WorkflowsResource", "AsyncWorkflowsResource"]


class WorkflowsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return WorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return WorkflowsResourceWithStreamingResponse(self)

    def cancel(
        self,
        key: str,
        *,
        cancellation_key: str,
        recipients: Optional[List[RecipientReferenceParam]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        When invoked for a workflow using a specific workflow key and cancellation key,
        will cancel any queued workflow runs associated with that key/cancellation key
        pair. Can optionally be provided one or more recipients to scope the request to.

        Args:
          cancellation_key: An optional key that is used to reference a specific workflow trigger request
              when issuing a [workflow cancellation](/send-notifications/canceling-workflows)
              request. Must be provided while triggering a workflow in order to enable
              subsequent cancellation. Should be unique across trigger requests to avoid
              unintentional cancellations.

          recipients: A list of recipients to cancel the notification for. If omitted, cancels for all
              recipients associated with the cancellation key.

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
        recipients: List[RecipientRequestParam],
        actor: Optional[RecipientRequestParam] | NotGiven = NOT_GIVEN,
        cancellation_key: Optional[str] | NotGiven = NOT_GIVEN,
        data: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        tenant: Optional[InlineTenantRequestParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowTriggerResponse:
        """
        Trigger a workflow (specified by the key) to run for the given recipients, using
        the parameters provided. Returns an identifier for the workflow run request. All
        workflow runs are executed asynchronously. This endpoint also handles
        [inline identifications](/managing-recipients/identifying-recipients#inline-identifying-recipients)
        for the `actor`, `recipient`, and `tenant` fields.

        Args:
          recipients: The recipients to trigger the workflow for. Can inline identify users, objects,
              or use a list of user IDs. Limited to 1,000 recipients.

          actor: Specifies a recipient in a request. This can either be a user identifier
              (string), an inline user request (object), or an inline object request, which is
              determined by the presence of a `collection` property.

          cancellation_key: An optional key that is used to reference a specific workflow trigger request
              when issuing a [workflow cancellation](/send-notifications/canceling-workflows)
              request. Must be provided while triggering a workflow in order to enable
              subsequent cancellation. Should be unique across trigger requests to avoid
              unintentional cancellations.

          data: An optional map of data to pass into the workflow execution. There is a 1024
              byte limit on the size of any single string value (with the exception of
              [email attachments](/integrations/email/attachments)), and a 10MB limit on the
              size of the full `data` payload.

          tenant: An request to set a tenant inline.

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
                    "recipients": recipients,
                    "actor": actor,
                    "cancellation_key": cancellation_key,
                    "data": data,
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

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncWorkflowsResourceWithStreamingResponse(self)

    async def cancel(
        self,
        key: str,
        *,
        cancellation_key: str,
        recipients: Optional[List[RecipientReferenceParam]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        When invoked for a workflow using a specific workflow key and cancellation key,
        will cancel any queued workflow runs associated with that key/cancellation key
        pair. Can optionally be provided one or more recipients to scope the request to.

        Args:
          cancellation_key: An optional key that is used to reference a specific workflow trigger request
              when issuing a [workflow cancellation](/send-notifications/canceling-workflows)
              request. Must be provided while triggering a workflow in order to enable
              subsequent cancellation. Should be unique across trigger requests to avoid
              unintentional cancellations.

          recipients: A list of recipients to cancel the notification for. If omitted, cancels for all
              recipients associated with the cancellation key.

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
        recipients: List[RecipientRequestParam],
        actor: Optional[RecipientRequestParam] | NotGiven = NOT_GIVEN,
        cancellation_key: Optional[str] | NotGiven = NOT_GIVEN,
        data: Optional[Dict[str, object]] | NotGiven = NOT_GIVEN,
        tenant: Optional[InlineTenantRequestParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowTriggerResponse:
        """
        Trigger a workflow (specified by the key) to run for the given recipients, using
        the parameters provided. Returns an identifier for the workflow run request. All
        workflow runs are executed asynchronously. This endpoint also handles
        [inline identifications](/managing-recipients/identifying-recipients#inline-identifying-recipients)
        for the `actor`, `recipient`, and `tenant` fields.

        Args:
          recipients: The recipients to trigger the workflow for. Can inline identify users, objects,
              or use a list of user IDs. Limited to 1,000 recipients.

          actor: Specifies a recipient in a request. This can either be a user identifier
              (string), an inline user request (object), or an inline object request, which is
              determined by the presence of a `collection` property.

          cancellation_key: An optional key that is used to reference a specific workflow trigger request
              when issuing a [workflow cancellation](/send-notifications/canceling-workflows)
              request. Must be provided while triggering a workflow in order to enable
              subsequent cancellation. Should be unique across trigger requests to avoid
              unintentional cancellations.

          data: An optional map of data to pass into the workflow execution. There is a 1024
              byte limit on the size of any single string value (with the exception of
              [email attachments](/integrations/email/attachments)), and a 10MB limit on the
              size of the full `data` payload.

          tenant: An request to set a tenant inline.

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
                    "recipients": recipients,
                    "actor": actor,
                    "cancellation_key": cancellation_key,
                    "data": data,
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
