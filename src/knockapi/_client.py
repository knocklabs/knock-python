# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import KnockError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        users,
        objects,
        tenants,
        channels,
        messages,
        audiences,
        providers,
        schedules,
        workflows,
        integrations,
        bulk_operations,
    )
    from .resources.audiences import AudiencesResource, AsyncAudiencesResource
    from .resources.workflows import WorkflowsResource, AsyncWorkflowsResource
    from .resources.users.users import UsersResource, AsyncUsersResource
    from .resources.bulk_operations import BulkOperationsResource, AsyncBulkOperationsResource
    from .resources.objects.objects import ObjectsResource, AsyncObjectsResource
    from .resources.tenants.tenants import TenantsResource, AsyncTenantsResource
    from .resources.channels.channels import ChannelsResource, AsyncChannelsResource
    from .resources.messages.messages import MessagesResource, AsyncMessagesResource
    from .resources.providers.providers import ProvidersResource, AsyncProvidersResource
    from .resources.schedules.schedules import SchedulesResource, AsyncSchedulesResource
    from .resources.integrations.integrations import IntegrationsResource, AsyncIntegrationsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Knock", "AsyncKnock", "Client", "AsyncClient"]


class Knock(SyncAPIClient):
    # client options
    api_key: str
    branch: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        branch: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Knock client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `KNOCK_API_KEY`
        - `branch` from `KNOCK_BRANCH`
        """
        if api_key is None:
            api_key = os.environ.get("KNOCK_API_KEY")
        if api_key is None:
            raise KnockError(
                "The api_key client option must be set either by passing api_key to the client or by setting the KNOCK_API_KEY environment variable"
            )
        self.api_key = api_key

        if branch is None:
            branch = os.environ.get("KNOCK_BRANCH")
        self.branch = branch

        if base_url is None:
            base_url = os.environ.get("KNOCK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.knock.app"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

    @cached_property
    def users(self) -> UsersResource:
        """A user is an individual from your system, represented in Knock.

        They are most commonly a recipient of a notification.
        """
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def objects(self) -> ObjectsResource:
        """An object represents a resource in your system that you want to map into Knock."""
        from .resources.objects import ObjectsResource

        return ObjectsResource(self)

    @cached_property
    def tenants(self) -> TenantsResource:
        """
        A tenant represents a top-level entity from your system, like a company, organization, account, or workspace.
        """
        from .resources.tenants import TenantsResource

        return TenantsResource(self)

    @cached_property
    def bulk_operations(self) -> BulkOperationsResource:
        """
        A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
        """
        from .resources.bulk_operations import BulkOperationsResource

        return BulkOperationsResource(self)

    @cached_property
    def messages(self) -> MessagesResource:
        """A message sent to a single recipient on a channel."""
        from .resources.messages import MessagesResource

        return MessagesResource(self)

    @cached_property
    def providers(self) -> ProvidersResource:
        from .resources.providers import ProvidersResource

        return ProvidersResource(self)

    @cached_property
    def integrations(self) -> IntegrationsResource:
        from .resources.integrations import IntegrationsResource

        return IntegrationsResource(self)

    @cached_property
    def workflows(self) -> WorkflowsResource:
        """
        A workflow is a structured set of steps that is triggered to produce notifications sent over channels.
        """
        from .resources.workflows import WorkflowsResource

        return WorkflowsResource(self)

    @cached_property
    def schedules(self) -> SchedulesResource:
        """
        A schedule is a per-recipient, timezone-aware configuration for when to invoke a workflow.
        """
        from .resources.schedules import SchedulesResource

        return SchedulesResource(self)

    @cached_property
    def channels(self) -> ChannelsResource:
        from .resources.channels import ChannelsResource

        return ChannelsResource(self)

    @cached_property
    def audiences(self) -> AudiencesResource:
        """An Audience is a segment of users."""
        from .resources.audiences import AudiencesResource

        return AudiencesResource(self)

    @cached_property
    def with_raw_response(self) -> KnockWithRawResponse:
        return KnockWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnockWithStreamedResponse:
        return KnockWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "X-Knock-Branch": self.branch if self.branch is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        branch: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            branch=branch or self.branch,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncKnock(AsyncAPIClient):
    # client options
    api_key: str
    branch: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        branch: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncKnock client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `KNOCK_API_KEY`
        - `branch` from `KNOCK_BRANCH`
        """
        if api_key is None:
            api_key = os.environ.get("KNOCK_API_KEY")
        if api_key is None:
            raise KnockError(
                "The api_key client option must be set either by passing api_key to the client or by setting the KNOCK_API_KEY environment variable"
            )
        self.api_key = api_key

        if branch is None:
            branch = os.environ.get("KNOCK_BRANCH")
        self.branch = branch

        if base_url is None:
            base_url = os.environ.get("KNOCK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.knock.app"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

    @cached_property
    def users(self) -> AsyncUsersResource:
        """A user is an individual from your system, represented in Knock.

        They are most commonly a recipient of a notification.
        """
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def objects(self) -> AsyncObjectsResource:
        """An object represents a resource in your system that you want to map into Knock."""
        from .resources.objects import AsyncObjectsResource

        return AsyncObjectsResource(self)

    @cached_property
    def tenants(self) -> AsyncTenantsResource:
        """
        A tenant represents a top-level entity from your system, like a company, organization, account, or workspace.
        """
        from .resources.tenants import AsyncTenantsResource

        return AsyncTenantsResource(self)

    @cached_property
    def bulk_operations(self) -> AsyncBulkOperationsResource:
        """
        A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
        """
        from .resources.bulk_operations import AsyncBulkOperationsResource

        return AsyncBulkOperationsResource(self)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        """A message sent to a single recipient on a channel."""
        from .resources.messages import AsyncMessagesResource

        return AsyncMessagesResource(self)

    @cached_property
    def providers(self) -> AsyncProvidersResource:
        from .resources.providers import AsyncProvidersResource

        return AsyncProvidersResource(self)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResource:
        from .resources.integrations import AsyncIntegrationsResource

        return AsyncIntegrationsResource(self)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResource:
        """
        A workflow is a structured set of steps that is triggered to produce notifications sent over channels.
        """
        from .resources.workflows import AsyncWorkflowsResource

        return AsyncWorkflowsResource(self)

    @cached_property
    def schedules(self) -> AsyncSchedulesResource:
        """
        A schedule is a per-recipient, timezone-aware configuration for when to invoke a workflow.
        """
        from .resources.schedules import AsyncSchedulesResource

        return AsyncSchedulesResource(self)

    @cached_property
    def channels(self) -> AsyncChannelsResource:
        from .resources.channels import AsyncChannelsResource

        return AsyncChannelsResource(self)

    @cached_property
    def audiences(self) -> AsyncAudiencesResource:
        """An Audience is a segment of users."""
        from .resources.audiences import AsyncAudiencesResource

        return AsyncAudiencesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncKnockWithRawResponse:
        return AsyncKnockWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKnockWithStreamedResponse:
        return AsyncKnockWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "X-Knock-Branch": self.branch if self.branch is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        branch: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            branch=branch or self.branch,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class KnockWithRawResponse:
    _client: Knock

    def __init__(self, client: Knock) -> None:
        self._client = client

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        """A user is an individual from your system, represented in Knock.

        They are most commonly a recipient of a notification.
        """
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def objects(self) -> objects.ObjectsResourceWithRawResponse:
        """An object represents a resource in your system that you want to map into Knock."""
        from .resources.objects import ObjectsResourceWithRawResponse

        return ObjectsResourceWithRawResponse(self._client.objects)

    @cached_property
    def tenants(self) -> tenants.TenantsResourceWithRawResponse:
        """
        A tenant represents a top-level entity from your system, like a company, organization, account, or workspace.
        """
        from .resources.tenants import TenantsResourceWithRawResponse

        return TenantsResourceWithRawResponse(self._client.tenants)

    @cached_property
    def bulk_operations(self) -> bulk_operations.BulkOperationsResourceWithRawResponse:
        """
        A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
        """
        from .resources.bulk_operations import BulkOperationsResourceWithRawResponse

        return BulkOperationsResourceWithRawResponse(self._client.bulk_operations)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        """A message sent to a single recipient on a channel."""
        from .resources.messages import MessagesResourceWithRawResponse

        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def providers(self) -> providers.ProvidersResourceWithRawResponse:
        from .resources.providers import ProvidersResourceWithRawResponse

        return ProvidersResourceWithRawResponse(self._client.providers)

    @cached_property
    def integrations(self) -> integrations.IntegrationsResourceWithRawResponse:
        from .resources.integrations import IntegrationsResourceWithRawResponse

        return IntegrationsResourceWithRawResponse(self._client.integrations)

    @cached_property
    def workflows(self) -> workflows.WorkflowsResourceWithRawResponse:
        """
        A workflow is a structured set of steps that is triggered to produce notifications sent over channels.
        """
        from .resources.workflows import WorkflowsResourceWithRawResponse

        return WorkflowsResourceWithRawResponse(self._client.workflows)

    @cached_property
    def schedules(self) -> schedules.SchedulesResourceWithRawResponse:
        """
        A schedule is a per-recipient, timezone-aware configuration for when to invoke a workflow.
        """
        from .resources.schedules import SchedulesResourceWithRawResponse

        return SchedulesResourceWithRawResponse(self._client.schedules)

    @cached_property
    def channels(self) -> channels.ChannelsResourceWithRawResponse:
        from .resources.channels import ChannelsResourceWithRawResponse

        return ChannelsResourceWithRawResponse(self._client.channels)

    @cached_property
    def audiences(self) -> audiences.AudiencesResourceWithRawResponse:
        """An Audience is a segment of users."""
        from .resources.audiences import AudiencesResourceWithRawResponse

        return AudiencesResourceWithRawResponse(self._client.audiences)


class AsyncKnockWithRawResponse:
    _client: AsyncKnock

    def __init__(self, client: AsyncKnock) -> None:
        self._client = client

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        """A user is an individual from your system, represented in Knock.

        They are most commonly a recipient of a notification.
        """
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def objects(self) -> objects.AsyncObjectsResourceWithRawResponse:
        """An object represents a resource in your system that you want to map into Knock."""
        from .resources.objects import AsyncObjectsResourceWithRawResponse

        return AsyncObjectsResourceWithRawResponse(self._client.objects)

    @cached_property
    def tenants(self) -> tenants.AsyncTenantsResourceWithRawResponse:
        """
        A tenant represents a top-level entity from your system, like a company, organization, account, or workspace.
        """
        from .resources.tenants import AsyncTenantsResourceWithRawResponse

        return AsyncTenantsResourceWithRawResponse(self._client.tenants)

    @cached_property
    def bulk_operations(self) -> bulk_operations.AsyncBulkOperationsResourceWithRawResponse:
        """
        A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
        """
        from .resources.bulk_operations import AsyncBulkOperationsResourceWithRawResponse

        return AsyncBulkOperationsResourceWithRawResponse(self._client.bulk_operations)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        """A message sent to a single recipient on a channel."""
        from .resources.messages import AsyncMessagesResourceWithRawResponse

        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def providers(self) -> providers.AsyncProvidersResourceWithRawResponse:
        from .resources.providers import AsyncProvidersResourceWithRawResponse

        return AsyncProvidersResourceWithRawResponse(self._client.providers)

    @cached_property
    def integrations(self) -> integrations.AsyncIntegrationsResourceWithRawResponse:
        from .resources.integrations import AsyncIntegrationsResourceWithRawResponse

        return AsyncIntegrationsResourceWithRawResponse(self._client.integrations)

    @cached_property
    def workflows(self) -> workflows.AsyncWorkflowsResourceWithRawResponse:
        """
        A workflow is a structured set of steps that is triggered to produce notifications sent over channels.
        """
        from .resources.workflows import AsyncWorkflowsResourceWithRawResponse

        return AsyncWorkflowsResourceWithRawResponse(self._client.workflows)

    @cached_property
    def schedules(self) -> schedules.AsyncSchedulesResourceWithRawResponse:
        """
        A schedule is a per-recipient, timezone-aware configuration for when to invoke a workflow.
        """
        from .resources.schedules import AsyncSchedulesResourceWithRawResponse

        return AsyncSchedulesResourceWithRawResponse(self._client.schedules)

    @cached_property
    def channels(self) -> channels.AsyncChannelsResourceWithRawResponse:
        from .resources.channels import AsyncChannelsResourceWithRawResponse

        return AsyncChannelsResourceWithRawResponse(self._client.channels)

    @cached_property
    def audiences(self) -> audiences.AsyncAudiencesResourceWithRawResponse:
        """An Audience is a segment of users."""
        from .resources.audiences import AsyncAudiencesResourceWithRawResponse

        return AsyncAudiencesResourceWithRawResponse(self._client.audiences)


class KnockWithStreamedResponse:
    _client: Knock

    def __init__(self, client: Knock) -> None:
        self._client = client

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        """A user is an individual from your system, represented in Knock.

        They are most commonly a recipient of a notification.
        """
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def objects(self) -> objects.ObjectsResourceWithStreamingResponse:
        """An object represents a resource in your system that you want to map into Knock."""
        from .resources.objects import ObjectsResourceWithStreamingResponse

        return ObjectsResourceWithStreamingResponse(self._client.objects)

    @cached_property
    def tenants(self) -> tenants.TenantsResourceWithStreamingResponse:
        """
        A tenant represents a top-level entity from your system, like a company, organization, account, or workspace.
        """
        from .resources.tenants import TenantsResourceWithStreamingResponse

        return TenantsResourceWithStreamingResponse(self._client.tenants)

    @cached_property
    def bulk_operations(self) -> bulk_operations.BulkOperationsResourceWithStreamingResponse:
        """
        A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
        """
        from .resources.bulk_operations import BulkOperationsResourceWithStreamingResponse

        return BulkOperationsResourceWithStreamingResponse(self._client.bulk_operations)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        """A message sent to a single recipient on a channel."""
        from .resources.messages import MessagesResourceWithStreamingResponse

        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def providers(self) -> providers.ProvidersResourceWithStreamingResponse:
        from .resources.providers import ProvidersResourceWithStreamingResponse

        return ProvidersResourceWithStreamingResponse(self._client.providers)

    @cached_property
    def integrations(self) -> integrations.IntegrationsResourceWithStreamingResponse:
        from .resources.integrations import IntegrationsResourceWithStreamingResponse

        return IntegrationsResourceWithStreamingResponse(self._client.integrations)

    @cached_property
    def workflows(self) -> workflows.WorkflowsResourceWithStreamingResponse:
        """
        A workflow is a structured set of steps that is triggered to produce notifications sent over channels.
        """
        from .resources.workflows import WorkflowsResourceWithStreamingResponse

        return WorkflowsResourceWithStreamingResponse(self._client.workflows)

    @cached_property
    def schedules(self) -> schedules.SchedulesResourceWithStreamingResponse:
        """
        A schedule is a per-recipient, timezone-aware configuration for when to invoke a workflow.
        """
        from .resources.schedules import SchedulesResourceWithStreamingResponse

        return SchedulesResourceWithStreamingResponse(self._client.schedules)

    @cached_property
    def channels(self) -> channels.ChannelsResourceWithStreamingResponse:
        from .resources.channels import ChannelsResourceWithStreamingResponse

        return ChannelsResourceWithStreamingResponse(self._client.channels)

    @cached_property
    def audiences(self) -> audiences.AudiencesResourceWithStreamingResponse:
        """An Audience is a segment of users."""
        from .resources.audiences import AudiencesResourceWithStreamingResponse

        return AudiencesResourceWithStreamingResponse(self._client.audiences)


class AsyncKnockWithStreamedResponse:
    _client: AsyncKnock

    def __init__(self, client: AsyncKnock) -> None:
        self._client = client

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        """A user is an individual from your system, represented in Knock.

        They are most commonly a recipient of a notification.
        """
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def objects(self) -> objects.AsyncObjectsResourceWithStreamingResponse:
        """An object represents a resource in your system that you want to map into Knock."""
        from .resources.objects import AsyncObjectsResourceWithStreamingResponse

        return AsyncObjectsResourceWithStreamingResponse(self._client.objects)

    @cached_property
    def tenants(self) -> tenants.AsyncTenantsResourceWithStreamingResponse:
        """
        A tenant represents a top-level entity from your system, like a company, organization, account, or workspace.
        """
        from .resources.tenants import AsyncTenantsResourceWithStreamingResponse

        return AsyncTenantsResourceWithStreamingResponse(self._client.tenants)

    @cached_property
    def bulk_operations(self) -> bulk_operations.AsyncBulkOperationsResourceWithStreamingResponse:
        """
        A bulk operation is a set of changes applied across zero or more records triggered via a call to the Knock API and performed asynchronously.
        """
        from .resources.bulk_operations import AsyncBulkOperationsResourceWithStreamingResponse

        return AsyncBulkOperationsResourceWithStreamingResponse(self._client.bulk_operations)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        """A message sent to a single recipient on a channel."""
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse

        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def providers(self) -> providers.AsyncProvidersResourceWithStreamingResponse:
        from .resources.providers import AsyncProvidersResourceWithStreamingResponse

        return AsyncProvidersResourceWithStreamingResponse(self._client.providers)

    @cached_property
    def integrations(self) -> integrations.AsyncIntegrationsResourceWithStreamingResponse:
        from .resources.integrations import AsyncIntegrationsResourceWithStreamingResponse

        return AsyncIntegrationsResourceWithStreamingResponse(self._client.integrations)

    @cached_property
    def workflows(self) -> workflows.AsyncWorkflowsResourceWithStreamingResponse:
        """
        A workflow is a structured set of steps that is triggered to produce notifications sent over channels.
        """
        from .resources.workflows import AsyncWorkflowsResourceWithStreamingResponse

        return AsyncWorkflowsResourceWithStreamingResponse(self._client.workflows)

    @cached_property
    def schedules(self) -> schedules.AsyncSchedulesResourceWithStreamingResponse:
        """
        A schedule is a per-recipient, timezone-aware configuration for when to invoke a workflow.
        """
        from .resources.schedules import AsyncSchedulesResourceWithStreamingResponse

        return AsyncSchedulesResourceWithStreamingResponse(self._client.schedules)

    @cached_property
    def channels(self) -> channels.AsyncChannelsResourceWithStreamingResponse:
        from .resources.channels import AsyncChannelsResourceWithStreamingResponse

        return AsyncChannelsResourceWithStreamingResponse(self._client.channels)

    @cached_property
    def audiences(self) -> audiences.AsyncAudiencesResourceWithStreamingResponse:
        """An Audience is a segment of users."""
        from .resources.audiences import AsyncAudiencesResourceWithStreamingResponse

        return AsyncAudiencesResourceWithStreamingResponse(self._client.audiences)


Client = Knock

AsyncClient = AsyncKnock
