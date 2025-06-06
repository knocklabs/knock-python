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
        bulk = client.objects.bulk.delete(
            collection="collection",
            object_ids=["obj_123", "obj_456", "obj_789"],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_delete(self, client: Knock) -> None:
        response = client.objects.bulk.with_raw_response.delete(
            collection="collection",
            object_ids=["obj_123", "obj_456", "obj_789"],
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
        with client.objects.bulk.with_streaming_response.delete(
            collection="collection",
            object_ids=["obj_123", "obj_456", "obj_789"],
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
    def test_path_params_delete(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.bulk.with_raw_response.delete(
                collection="",
                object_ids=["obj_123", "obj_456", "obj_789"],
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_add_subscriptions(self, client: Knock) -> None:
        bulk = client.objects.bulk.add_subscriptions(
            collection="projects",
            subscriptions=[{"recipients": [{"id": "user_1"}]}],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_add_subscriptions(self, client: Knock) -> None:
        response = client.objects.bulk.with_raw_response.add_subscriptions(
            collection="projects",
            subscriptions=[{"recipients": [{"id": "user_1"}]}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_add_subscriptions(self, client: Knock) -> None:
        with client.objects.bulk.with_streaming_response.add_subscriptions(
            collection="projects",
            subscriptions=[{"recipients": [{"id": "user_1"}]}],
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
    def test_path_params_add_subscriptions(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.bulk.with_raw_response.add_subscriptions(
                collection="",
                subscriptions=[{"recipients": [{"id": "user_1"}]}],
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_set(self, client: Knock) -> None:
        bulk = client.objects.bulk.set(
            collection="collection",
            objects=[{"id": "project_1"}],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_set(self, client: Knock) -> None:
        response = client.objects.bulk.with_raw_response.set(
            collection="collection",
            objects=[{"id": "project_1"}],
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
        with client.objects.bulk.with_streaming_response.set(
            collection="collection",
            objects=[{"id": "project_1"}],
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
    def test_path_params_set(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.bulk.with_raw_response.set(
                collection="",
                objects=[{"id": "project_1"}],
            )


class TestAsyncBulk:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_delete(self, async_client: AsyncKnock) -> None:
        bulk = await async_client.objects.bulk.delete(
            collection="collection",
            object_ids=["obj_123", "obj_456", "obj_789"],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.bulk.with_raw_response.delete(
            collection="collection",
            object_ids=["obj_123", "obj_456", "obj_789"],
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
        async with async_client.objects.bulk.with_streaming_response.delete(
            collection="collection",
            object_ids=["obj_123", "obj_456", "obj_789"],
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
    async def test_path_params_delete(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.bulk.with_raw_response.delete(
                collection="",
                object_ids=["obj_123", "obj_456", "obj_789"],
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_add_subscriptions(self, async_client: AsyncKnock) -> None:
        bulk = await async_client.objects.bulk.add_subscriptions(
            collection="projects",
            subscriptions=[{"recipients": [{"id": "user_1"}]}],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_add_subscriptions(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.bulk.with_raw_response.add_subscriptions(
            collection="projects",
            subscriptions=[{"recipients": [{"id": "user_1"}]}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_add_subscriptions(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.bulk.with_streaming_response.add_subscriptions(
            collection="projects",
            subscriptions=[{"recipients": [{"id": "user_1"}]}],
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
    async def test_path_params_add_subscriptions(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.bulk.with_raw_response.add_subscriptions(
                collection="",
                subscriptions=[{"recipients": [{"id": "user_1"}]}],
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_set(self, async_client: AsyncKnock) -> None:
        bulk = await async_client.objects.bulk.set(
            collection="collection",
            objects=[{"id": "project_1"}],
        )
        assert_matches_type(BulkOperation, bulk, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_set(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.bulk.with_raw_response.set(
            collection="collection",
            objects=[{"id": "project_1"}],
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
        async with async_client.objects.bulk.with_streaming_response.set(
            collection="collection",
            objects=[{"id": "project_1"}],
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
    async def test_path_params_set(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.bulk.with_raw_response.set(
                collection="",
                objects=[{"id": "project_1"}],
            )
