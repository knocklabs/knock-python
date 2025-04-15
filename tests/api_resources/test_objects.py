# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.types import (
    Object,
    ObjectAddSubscriptionsResponse,
    ObjectDeleteSubscriptionsResponse,
)
from knockapi.pagination import SyncEntriesCursor, AsyncEntriesCursor
from knockapi.types.recipients import ChannelData, Subscription

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestObjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list(self, client: Knock) -> None:
        object_ = client.objects.list(
            collection="collection",
        )
        assert_matches_type(SyncEntriesCursor[Object], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_with_all_params(self, client: Knock) -> None:
        object_ = client.objects.list(
            collection="collection",
            after="after",
            before="before",
            page_size=0,
        )
        assert_matches_type(SyncEntriesCursor[Object], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list(self, client: Knock) -> None:
        response = client.objects.with_raw_response.list(
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(SyncEntriesCursor[Object], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list(self, client: Knock) -> None:
        with client.objects.with_streaming_response.list(
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(SyncEntriesCursor[Object], object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.list(
                collection="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_add_subscriptions(self, client: Knock) -> None:
        object_ = client.objects.add_subscriptions(
            collection="collection",
            object_id="object_id",
            recipients=["user_1", "user_2"],
        )
        assert_matches_type(ObjectAddSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_add_subscriptions_with_all_params(self, client: Knock) -> None:
        object_ = client.objects.add_subscriptions(
            collection="collection",
            object_id="object_id",
            recipients=["user_1", "user_2"],
            properties={"key": "bar"},
        )
        assert_matches_type(ObjectAddSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_add_subscriptions(self, client: Knock) -> None:
        response = client.objects.with_raw_response.add_subscriptions(
            collection="collection",
            object_id="object_id",
            recipients=["user_1", "user_2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectAddSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_add_subscriptions(self, client: Knock) -> None:
        with client.objects.with_streaming_response.add_subscriptions(
            collection="collection",
            object_id="object_id",
            recipients=["user_1", "user_2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectAddSubscriptionsResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_add_subscriptions(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.add_subscriptions(
                collection="",
                object_id="object_id",
                recipients=["user_1", "user_2"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.objects.with_raw_response.add_subscriptions(
                collection="collection",
                object_id="",
                recipients=["user_1", "user_2"],
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_delete_subscriptions(self, client: Knock) -> None:
        object_ = client.objects.delete_subscriptions(
            collection="collection",
            object_id="object_id",
            recipients=[{"id": "user_1"}],
        )
        assert_matches_type(ObjectDeleteSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_delete_subscriptions(self, client: Knock) -> None:
        response = client.objects.with_raw_response.delete_subscriptions(
            collection="collection",
            object_id="object_id",
            recipients=[{"id": "user_1"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectDeleteSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_delete_subscriptions(self, client: Knock) -> None:
        with client.objects.with_streaming_response.delete_subscriptions(
            collection="collection",
            object_id="object_id",
            recipients=[{"id": "user_1"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectDeleteSubscriptionsResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_delete_subscriptions(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.delete_subscriptions(
                collection="",
                object_id="object_id",
                recipients=[{"id": "user_1"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.objects.with_raw_response.delete_subscriptions(
                collection="collection",
                object_id="",
                recipients=[{"id": "user_1"}],
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_get_channel_data(self, client: Knock) -> None:
        object_ = client.objects.get_channel_data(
            collection="collection",
            object_id="object_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChannelData, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_get_channel_data(self, client: Knock) -> None:
        response = client.objects.with_raw_response.get_channel_data(
            collection="collection",
            object_id="object_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ChannelData, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_get_channel_data(self, client: Knock) -> None:
        with client.objects.with_streaming_response.get_channel_data(
            collection="collection",
            object_id="object_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ChannelData, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_get_channel_data(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.get_channel_data(
                collection="",
                object_id="object_id",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.objects.with_raw_response.get_channel_data(
                collection="collection",
                object_id="",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.objects.with_raw_response.get_channel_data(
                collection="collection",
                object_id="object_id",
                channel_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_subscriptions(self, client: Knock) -> None:
        object_ = client.objects.list_subscriptions(
            collection="collection",
            object_id="object_id",
        )
        assert_matches_type(SyncEntriesCursor[Subscription], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_subscriptions_with_all_params(self, client: Knock) -> None:
        object_ = client.objects.list_subscriptions(
            collection="collection",
            object_id="object_id",
            after="after",
            before="before",
            mode="recipient",
            objects=["user_123"],
            page_size=0,
            recipients=["user_123"],
        )
        assert_matches_type(SyncEntriesCursor[Subscription], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list_subscriptions(self, client: Knock) -> None:
        response = client.objects.with_raw_response.list_subscriptions(
            collection="collection",
            object_id="object_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(SyncEntriesCursor[Subscription], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list_subscriptions(self, client: Knock) -> None:
        with client.objects.with_streaming_response.list_subscriptions(
            collection="collection",
            object_id="object_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(SyncEntriesCursor[Subscription], object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list_subscriptions(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.list_subscriptions(
                collection="",
                object_id="object_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.objects.with_raw_response.list_subscriptions(
                collection="collection",
                object_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_set_channel_data(self, client: Knock) -> None:
        object_ = client.objects.set_channel_data(
            collection="collection",
            object_id="object_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChannelData, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_set_channel_data(self, client: Knock) -> None:
        response = client.objects.with_raw_response.set_channel_data(
            collection="collection",
            object_id="object_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ChannelData, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_set_channel_data(self, client: Knock) -> None:
        with client.objects.with_streaming_response.set_channel_data(
            collection="collection",
            object_id="object_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ChannelData, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_set_channel_data(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.set_channel_data(
                collection="",
                object_id="object_id",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.objects.with_raw_response.set_channel_data(
                collection="collection",
                object_id="",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.objects.with_raw_response.set_channel_data(
                collection="collection",
                object_id="object_id",
                channel_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_unset_channel_data(self, client: Knock) -> None:
        object_ = client.objects.unset_channel_data(
            collection="collection",
            object_id="object_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_unset_channel_data(self, client: Knock) -> None:
        response = client.objects.with_raw_response.unset_channel_data(
            collection="collection",
            object_id="object_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(str, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_unset_channel_data(self, client: Knock) -> None:
        with client.objects.with_streaming_response.unset_channel_data(
            collection="collection",
            object_id="object_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(str, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_unset_channel_data(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            client.objects.with_raw_response.unset_channel_data(
                collection="",
                object_id="object_id",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.objects.with_raw_response.unset_channel_data(
                collection="collection",
                object_id="",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.objects.with_raw_response.unset_channel_data(
                collection="collection",
                object_id="object_id",
                channel_id="",
            )


class TestAsyncObjects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.list(
            collection="collection",
        )
        assert_matches_type(AsyncEntriesCursor[Object], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.list(
            collection="collection",
            after="after",
            before="before",
            page_size=0,
        )
        assert_matches_type(AsyncEntriesCursor[Object], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.list(
            collection="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(AsyncEntriesCursor[Object], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.list(
            collection="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(AsyncEntriesCursor[Object], object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.list(
                collection="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_add_subscriptions(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.add_subscriptions(
            collection="collection",
            object_id="object_id",
            recipients=["user_1", "user_2"],
        )
        assert_matches_type(ObjectAddSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_add_subscriptions_with_all_params(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.add_subscriptions(
            collection="collection",
            object_id="object_id",
            recipients=["user_1", "user_2"],
            properties={"key": "bar"},
        )
        assert_matches_type(ObjectAddSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_add_subscriptions(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.add_subscriptions(
            collection="collection",
            object_id="object_id",
            recipients=["user_1", "user_2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectAddSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_add_subscriptions(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.add_subscriptions(
            collection="collection",
            object_id="object_id",
            recipients=["user_1", "user_2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectAddSubscriptionsResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_add_subscriptions(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.add_subscriptions(
                collection="",
                object_id="object_id",
                recipients=["user_1", "user_2"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.objects.with_raw_response.add_subscriptions(
                collection="collection",
                object_id="",
                recipients=["user_1", "user_2"],
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_delete_subscriptions(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.delete_subscriptions(
            collection="collection",
            object_id="object_id",
            recipients=[{"id": "user_1"}],
        )
        assert_matches_type(ObjectDeleteSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_delete_subscriptions(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.delete_subscriptions(
            collection="collection",
            object_id="object_id",
            recipients=[{"id": "user_1"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectDeleteSubscriptionsResponse, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_delete_subscriptions(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.delete_subscriptions(
            collection="collection",
            object_id="object_id",
            recipients=[{"id": "user_1"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectDeleteSubscriptionsResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_delete_subscriptions(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.delete_subscriptions(
                collection="",
                object_id="object_id",
                recipients=[{"id": "user_1"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.objects.with_raw_response.delete_subscriptions(
                collection="collection",
                object_id="",
                recipients=[{"id": "user_1"}],
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_get_channel_data(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.get_channel_data(
            collection="collection",
            object_id="object_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChannelData, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_get_channel_data(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.get_channel_data(
            collection="collection",
            object_id="object_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ChannelData, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_get_channel_data(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.get_channel_data(
            collection="collection",
            object_id="object_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ChannelData, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_get_channel_data(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.get_channel_data(
                collection="",
                object_id="object_id",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.objects.with_raw_response.get_channel_data(
                collection="collection",
                object_id="",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.objects.with_raw_response.get_channel_data(
                collection="collection",
                object_id="object_id",
                channel_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_subscriptions(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.list_subscriptions(
            collection="collection",
            object_id="object_id",
        )
        assert_matches_type(AsyncEntriesCursor[Subscription], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_subscriptions_with_all_params(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.list_subscriptions(
            collection="collection",
            object_id="object_id",
            after="after",
            before="before",
            mode="recipient",
            objects=["user_123"],
            page_size=0,
            recipients=["user_123"],
        )
        assert_matches_type(AsyncEntriesCursor[Subscription], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list_subscriptions(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.list_subscriptions(
            collection="collection",
            object_id="object_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(AsyncEntriesCursor[Subscription], object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list_subscriptions(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.list_subscriptions(
            collection="collection",
            object_id="object_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(AsyncEntriesCursor[Subscription], object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list_subscriptions(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.list_subscriptions(
                collection="",
                object_id="object_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.objects.with_raw_response.list_subscriptions(
                collection="collection",
                object_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_set_channel_data(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.set_channel_data(
            collection="collection",
            object_id="object_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ChannelData, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_set_channel_data(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.set_channel_data(
            collection="collection",
            object_id="object_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ChannelData, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_set_channel_data(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.set_channel_data(
            collection="collection",
            object_id="object_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ChannelData, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_set_channel_data(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.set_channel_data(
                collection="",
                object_id="object_id",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.objects.with_raw_response.set_channel_data(
                collection="collection",
                object_id="",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.objects.with_raw_response.set_channel_data(
                collection="collection",
                object_id="object_id",
                channel_id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_unset_channel_data(self, async_client: AsyncKnock) -> None:
        object_ = await async_client.objects.unset_channel_data(
            collection="collection",
            object_id="object_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(str, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_unset_channel_data(self, async_client: AsyncKnock) -> None:
        response = await async_client.objects.with_raw_response.unset_channel_data(
            collection="collection",
            object_id="object_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(str, object_, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_unset_channel_data(self, async_client: AsyncKnock) -> None:
        async with async_client.objects.with_streaming_response.unset_channel_data(
            collection="collection",
            object_id="object_id",
            channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(str, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_unset_channel_data(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `collection` but received ''"):
            await async_client.objects.with_raw_response.unset_channel_data(
                collection="",
                object_id="object_id",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.objects.with_raw_response.unset_channel_data(
                collection="collection",
                object_id="",
                channel_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.objects.with_raw_response.unset_channel_data(
                collection="collection",
                object_id="object_id",
                channel_id="",
            )
