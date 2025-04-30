# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .census import (
    CensusResource,
    AsyncCensusResource,
    CensusResourceWithRawResponse,
    AsyncCensusResourceWithRawResponse,
    CensusResourceWithStreamingResponse,
    AsyncCensusResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .hightouch import (
    HightouchResource,
    AsyncHightouchResource,
    HightouchResourceWithRawResponse,
    AsyncHightouchResourceWithRawResponse,
    HightouchResourceWithStreamingResponse,
    AsyncHightouchResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["IntegrationsResource", "AsyncIntegrationsResource"]


class IntegrationsResource(SyncAPIResource):
    @cached_property
    def census(self) -> CensusResource:
        return CensusResource(self._client)

    @cached_property
    def hightouch(self) -> HightouchResource:
        return HightouchResource(self._client)

    @cached_property
    def with_raw_response(self) -> IntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return IntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return IntegrationsResourceWithStreamingResponse(self)


class AsyncIntegrationsResource(AsyncAPIResource):
    @cached_property
    def census(self) -> AsyncCensusResource:
        return AsyncCensusResource(self._client)

    @cached_property
    def hightouch(self) -> AsyncHightouchResource:
        return AsyncHightouchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/knocklabs/knock-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/knocklabs/knock-python#with_streaming_response
        """
        return AsyncIntegrationsResourceWithStreamingResponse(self)


class IntegrationsResourceWithRawResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

    @cached_property
    def census(self) -> CensusResourceWithRawResponse:
        return CensusResourceWithRawResponse(self._integrations.census)

    @cached_property
    def hightouch(self) -> HightouchResourceWithRawResponse:
        return HightouchResourceWithRawResponse(self._integrations.hightouch)


class AsyncIntegrationsResourceWithRawResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

    @cached_property
    def census(self) -> AsyncCensusResourceWithRawResponse:
        return AsyncCensusResourceWithRawResponse(self._integrations.census)

    @cached_property
    def hightouch(self) -> AsyncHightouchResourceWithRawResponse:
        return AsyncHightouchResourceWithRawResponse(self._integrations.hightouch)


class IntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

    @cached_property
    def census(self) -> CensusResourceWithStreamingResponse:
        return CensusResourceWithStreamingResponse(self._integrations.census)

    @cached_property
    def hightouch(self) -> HightouchResourceWithStreamingResponse:
        return HightouchResourceWithStreamingResponse(self._integrations.hightouch)


class AsyncIntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

    @cached_property
    def census(self) -> AsyncCensusResourceWithStreamingResponse:
        return AsyncCensusResourceWithStreamingResponse(self._integrations.census)

    @cached_property
    def hightouch(self) -> AsyncHightouchResourceWithStreamingResponse:
        return AsyncHightouchResourceWithStreamingResponse(self._integrations.hightouch)
