# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .slack import (
    SlackResource,
    AsyncSlackResource,
    SlackResourceWithRawResponse,
    AsyncSlackResourceWithRawResponse,
    SlackResourceWithStreamingResponse,
    AsyncSlackResourceWithStreamingResponse,
)
from .ms_teams import (
    MsTeamsResource,
    AsyncMsTeamsResource,
    MsTeamsResourceWithRawResponse,
    AsyncMsTeamsResourceWithRawResponse,
    MsTeamsResourceWithStreamingResponse,
    AsyncMsTeamsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ProvidersResource", "AsyncProvidersResource"]


class ProvidersResource(SyncAPIResource):
    @cached_property
    def slack(self) -> SlackResource:
        return SlackResource(self._client)

    @cached_property
    def ms_teams(self) -> MsTeamsResource:
        return MsTeamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return ProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return ProvidersResourceWithStreamingResponse(self)


class AsyncProvidersResource(AsyncAPIResource):
    @cached_property
    def slack(self) -> AsyncSlackResource:
        return AsyncSlackResource(self._client)

    @cached_property
    def ms_teams(self) -> AsyncMsTeamsResource:
        return AsyncMsTeamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncProvidersResourceWithStreamingResponse(self)


class ProvidersResourceWithRawResponse:
    def __init__(self, providers: ProvidersResource) -> None:
        self._providers = providers

    @cached_property
    def slack(self) -> SlackResourceWithRawResponse:
        return SlackResourceWithRawResponse(self._providers.slack)

    @cached_property
    def ms_teams(self) -> MsTeamsResourceWithRawResponse:
        return MsTeamsResourceWithRawResponse(self._providers.ms_teams)


class AsyncProvidersResourceWithRawResponse:
    def __init__(self, providers: AsyncProvidersResource) -> None:
        self._providers = providers

    @cached_property
    def slack(self) -> AsyncSlackResourceWithRawResponse:
        return AsyncSlackResourceWithRawResponse(self._providers.slack)

    @cached_property
    def ms_teams(self) -> AsyncMsTeamsResourceWithRawResponse:
        return AsyncMsTeamsResourceWithRawResponse(self._providers.ms_teams)


class ProvidersResourceWithStreamingResponse:
    def __init__(self, providers: ProvidersResource) -> None:
        self._providers = providers

    @cached_property
    def slack(self) -> SlackResourceWithStreamingResponse:
        return SlackResourceWithStreamingResponse(self._providers.slack)

    @cached_property
    def ms_teams(self) -> MsTeamsResourceWithStreamingResponse:
        return MsTeamsResourceWithStreamingResponse(self._providers.ms_teams)


class AsyncProvidersResourceWithStreamingResponse:
    def __init__(self, providers: AsyncProvidersResource) -> None:
        self._providers = providers

    @cached_property
    def slack(self) -> AsyncSlackResourceWithStreamingResponse:
        return AsyncSlackResourceWithStreamingResponse(self._providers.slack)

    @cached_property
    def ms_teams(self) -> AsyncMsTeamsResourceWithStreamingResponse:
        return AsyncMsTeamsResourceWithStreamingResponse(self._providers.ms_teams)
