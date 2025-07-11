# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.types import BulkOperation
from knockapi._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulk:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_update_message_status(self, client: Knock) -> None:
        bulk = client.channels.bulk.update_message_status(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="seen",
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_update_message_status_with_all_params(self, client: Knock) -> None:
        bulk = client.channels.bulk.update_message_status(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="seen",
            archived="include",
            delivery_status="delivered",
            engagement_status="seen",
            has_tenant=True,
            newer_than=parse_datetime("2024-01-01T00:00:00Z"),
            older_than=parse_datetime("2024-01-01T00:00:00Z"),
            recipient_ids=["recipient1", "recipient2"],
            tenants=["tenant1", "tenant2"],
            trigger_data='{"key":"value"}',
            workflows=["workflow1", "workflow2"],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_update_message_status(self, client: Knock) -> None:
        response = client.channels.bulk.with_raw_response.update_message_status(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="seen",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_update_message_status(self, client: Knock) -> None:
        with client.channels.bulk.with_streaming_response.update_message_status(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="seen",
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
    def test_path_params_update_message_status(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.channels.bulk.with_raw_response.update_message_status(
                channel_id="",
                action="seen",
            )


class TestAsyncBulk:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_update_message_status(self, async_client: AsyncKnock) -> None:
        bulk = await async_client.channels.bulk.update_message_status(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="seen",
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_update_message_status_with_all_params(self, async_client: AsyncKnock) -> None:
        bulk = await async_client.channels.bulk.update_message_status(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="seen",
            archived="include",
            delivery_status="delivered",
            engagement_status="seen",
            has_tenant=True,
            newer_than=parse_datetime("2024-01-01T00:00:00Z"),
            older_than=parse_datetime("2024-01-01T00:00:00Z"),
            recipient_ids=["recipient1", "recipient2"],
            tenants=["tenant1", "tenant2"],
            trigger_data='{"key":"value"}',
            workflows=["workflow1", "workflow2"],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_update_message_status(self, async_client: AsyncKnock) -> None:
        response = await async_client.channels.bulk.with_raw_response.update_message_status(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="seen",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_update_message_status(self, async_client: AsyncKnock) -> None:
        async with async_client.channels.bulk.with_streaming_response.update_message_status(
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            action="seen",
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
    async def test_path_params_update_message_status(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.channels.bulk.with_raw_response.update_message_status(
                channel_id="",
                action="seen",
            )
