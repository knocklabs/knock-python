# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.types import BulkOperation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulk:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_delete(self, client: Knock) -> None:
        bulk = client.tenants.bulk.delete(
            tenant_ids=["string"],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_delete(self, client: Knock) -> None:
        response = client.tenants.bulk.with_raw_response.delete(
            tenant_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_delete(self, client: Knock) -> None:
        with client.tenants.bulk.with_streaming_response.delete(
            tenant_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkOperation, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_set(self, client: Knock) -> None:
        bulk = client.tenants.bulk.set(
            tenants=["string"],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_set(self, client: Knock) -> None:
        response = client.tenants.bulk.with_raw_response.set(
            tenants=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_set(self, client: Knock) -> None:
        with client.tenants.bulk.with_streaming_response.set(
            tenants=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkOperation, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBulk:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_delete(self, async_client: AsyncKnock) -> None:
        bulk = await async_client.tenants.bulk.delete(
            tenant_ids=["string"],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKnock) -> None:
        response = await async_client.tenants.bulk.with_raw_response.delete(
            tenant_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncKnock) -> None:
        async with async_client.tenants.bulk.with_streaming_response.delete(
            tenant_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkOperation, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_set(self, async_client: AsyncKnock) -> None:
        bulk = await async_client.tenants.bulk.set(
            tenants=["string"],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_set(self, async_client: AsyncKnock) -> None:
        response = await async_client.tenants.bulk.with_raw_response.set(
            tenants=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncKnock) -> None:
        async with async_client.tenants.bulk.with_streaming_response.set(
            tenants=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkOperation, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True
