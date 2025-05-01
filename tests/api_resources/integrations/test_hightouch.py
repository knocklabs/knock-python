# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.types.integrations import HightouchEmbeddedDestinationResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHightouch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_embedded_destination(self, client: Knock) -> None:
        hightouch = client.integrations.hightouch.embedded_destination(
            id="id",
            jsonrpc="jsonrpc",
            method="method",
        )
        assert_matches_type(HightouchEmbeddedDestinationResponse, hightouch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_embedded_destination_with_all_params(self, client: Knock) -> None:
        hightouch = client.integrations.hightouch.embedded_destination(
            id="id",
            jsonrpc="jsonrpc",
            method="method",
            params={"foo": "bar"},
        )
        assert_matches_type(HightouchEmbeddedDestinationResponse, hightouch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_embedded_destination(self, client: Knock) -> None:
        response = client.integrations.hightouch.with_raw_response.embedded_destination(
            id="id",
            jsonrpc="jsonrpc",
            method="method",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hightouch = response.parse()
        assert_matches_type(HightouchEmbeddedDestinationResponse, hightouch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_embedded_destination(self, client: Knock) -> None:
        with client.integrations.hightouch.with_streaming_response.embedded_destination(
            id="id",
            jsonrpc="jsonrpc",
            method="method",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hightouch = response.parse()
            assert_matches_type(HightouchEmbeddedDestinationResponse, hightouch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHightouch:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_embedded_destination(self, async_client: AsyncKnock) -> None:
        hightouch = await async_client.integrations.hightouch.embedded_destination(
            id="id",
            jsonrpc="jsonrpc",
            method="method",
        )
        assert_matches_type(HightouchEmbeddedDestinationResponse, hightouch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_embedded_destination_with_all_params(self, async_client: AsyncKnock) -> None:
        hightouch = await async_client.integrations.hightouch.embedded_destination(
            id="id",
            jsonrpc="jsonrpc",
            method="method",
            params={"foo": "bar"},
        )
        assert_matches_type(HightouchEmbeddedDestinationResponse, hightouch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_embedded_destination(self, async_client: AsyncKnock) -> None:
        response = await async_client.integrations.hightouch.with_raw_response.embedded_destination(
            id="id",
            jsonrpc="jsonrpc",
            method="method",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hightouch = await response.parse()
        assert_matches_type(HightouchEmbeddedDestinationResponse, hightouch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_embedded_destination(self, async_client: AsyncKnock) -> None:
        async with async_client.integrations.hightouch.with_streaming_response.embedded_destination(
            id="id",
            jsonrpc="jsonrpc",
            method="method",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hightouch = await response.parse()
            assert_matches_type(HightouchEmbeddedDestinationResponse, hightouch, path=["response"])

        assert cast(Any, response.is_closed) is True
