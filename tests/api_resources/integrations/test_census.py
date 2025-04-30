# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.types.integrations import CensusCustomDestinationResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCensus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_custom_destination(self, client: Knock) -> None:
        census = client.integrations.census.custom_destination(
            id="id",
            jsonrpc="jsonrpc",
            method="method",
        )
        assert_matches_type(CensusCustomDestinationResponse, census, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_custom_destination_with_all_params(self, client: Knock) -> None:
        census = client.integrations.census.custom_destination(
            id="id",
            jsonrpc="jsonrpc",
            method="method",
            params={"foo": "bar"},
        )
        assert_matches_type(CensusCustomDestinationResponse, census, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_custom_destination(self, client: Knock) -> None:
        response = client.integrations.census.with_raw_response.custom_destination(
            id="id",
            jsonrpc="jsonrpc",
            method="method",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        census = response.parse()
        assert_matches_type(CensusCustomDestinationResponse, census, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_custom_destination(self, client: Knock) -> None:
        with client.integrations.census.with_streaming_response.custom_destination(
            id="id",
            jsonrpc="jsonrpc",
            method="method",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            census = response.parse()
            assert_matches_type(CensusCustomDestinationResponse, census, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCensus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_custom_destination(self, async_client: AsyncKnock) -> None:
        census = await async_client.integrations.census.custom_destination(
            id="id",
            jsonrpc="jsonrpc",
            method="method",
        )
        assert_matches_type(CensusCustomDestinationResponse, census, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_custom_destination_with_all_params(self, async_client: AsyncKnock) -> None:
        census = await async_client.integrations.census.custom_destination(
            id="id",
            jsonrpc="jsonrpc",
            method="method",
            params={"foo": "bar"},
        )
        assert_matches_type(CensusCustomDestinationResponse, census, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_custom_destination(self, async_client: AsyncKnock) -> None:
        response = await async_client.integrations.census.with_raw_response.custom_destination(
            id="id",
            jsonrpc="jsonrpc",
            method="method",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        census = await response.parse()
        assert_matches_type(CensusCustomDestinationResponse, census, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_custom_destination(self, async_client: AsyncKnock) -> None:
        async with async_client.integrations.census.with_streaming_response.custom_destination(
            id="id",
            jsonrpc="jsonrpc",
            method="method",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            census = await response.parse()
            assert_matches_type(CensusCustomDestinationResponse, census, path=["response"])

        assert cast(Any, response.is_closed) is True
