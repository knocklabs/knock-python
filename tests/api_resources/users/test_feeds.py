# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.pagination import SyncEntriesCursor, AsyncEntriesCursor
from knockapi.types.users import FeedListItemsResponse, FeedGetSettingsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeeds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_get_settings(self, client: Knock) -> None:
        feed = client.users.feeds.get_settings(
            user_id="user_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FeedGetSettingsResponse, feed, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_get_settings(self, client: Knock) -> None:
        response = client.users.feeds.with_raw_response.get_settings(
            user_id="user_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feed = response.parse()
        assert_matches_type(FeedGetSettingsResponse, feed, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_get_settings(self, client: Knock) -> None:
        with client.users.feeds.with_streaming_response.get_settings(
            user_id="user_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feed = response.parse()
            assert_matches_type(FeedGetSettingsResponse, feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_get_settings(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.feeds.with_raw_response.get_settings(
                user_id="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.feeds.with_raw_response.get_settings(
                user_id="user_id",
                id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_items(self, client: Knock) -> None:
        feed = client.users.feeds.list_items(
            user_id="user_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncEntriesCursor[FeedListItemsResponse], feed, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_list_items_with_all_params(self, client: Knock) -> None:
        feed = client.users.feeds.list_items(
            user_id="user_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            archived="exclude",
            before="before",
            has_tenant=True,
            page_size=0,
            source="source",
            status="unread",
            tenant="tenant",
            trigger_data="trigger_data",
            workflow_categories=["string"],
        )
        assert_matches_type(SyncEntriesCursor[FeedListItemsResponse], feed, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_list_items(self, client: Knock) -> None:
        response = client.users.feeds.with_raw_response.list_items(
            user_id="user_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feed = response.parse()
        assert_matches_type(SyncEntriesCursor[FeedListItemsResponse], feed, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_list_items(self, client: Knock) -> None:
        with client.users.feeds.with_streaming_response.list_items(
            user_id="user_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feed = response.parse()
            assert_matches_type(SyncEntriesCursor[FeedListItemsResponse], feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_path_params_list_items(self, client: Knock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.feeds.with_raw_response.list_items(
                user_id="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.users.feeds.with_raw_response.list_items(
                user_id="user_id",
                id="",
            )


class TestAsyncFeeds:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_get_settings(self, async_client: AsyncKnock) -> None:
        feed = await async_client.users.feeds.get_settings(
            user_id="user_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FeedGetSettingsResponse, feed, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_get_settings(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.feeds.with_raw_response.get_settings(
            user_id="user_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feed = await response.parse()
        assert_matches_type(FeedGetSettingsResponse, feed, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_get_settings(self, async_client: AsyncKnock) -> None:
        async with async_client.users.feeds.with_streaming_response.get_settings(
            user_id="user_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feed = await response.parse()
            assert_matches_type(FeedGetSettingsResponse, feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_get_settings(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.feeds.with_raw_response.get_settings(
                user_id="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.feeds.with_raw_response.get_settings(
                user_id="user_id",
                id="",
            )

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_items(self, async_client: AsyncKnock) -> None:
        feed = await async_client.users.feeds.list_items(
            user_id="user_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncEntriesCursor[FeedListItemsResponse], feed, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_list_items_with_all_params(self, async_client: AsyncKnock) -> None:
        feed = await async_client.users.feeds.list_items(
            user_id="user_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            archived="exclude",
            before="before",
            has_tenant=True,
            page_size=0,
            source="source",
            status="unread",
            tenant="tenant",
            trigger_data="trigger_data",
            workflow_categories=["string"],
        )
        assert_matches_type(AsyncEntriesCursor[FeedListItemsResponse], feed, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_list_items(self, async_client: AsyncKnock) -> None:
        response = await async_client.users.feeds.with_raw_response.list_items(
            user_id="user_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feed = await response.parse()
        assert_matches_type(AsyncEntriesCursor[FeedListItemsResponse], feed, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_list_items(self, async_client: AsyncKnock) -> None:
        async with async_client.users.feeds.with_streaming_response.list_items(
            user_id="user_id",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feed = await response.parse()
            assert_matches_type(AsyncEntriesCursor[FeedListItemsResponse], feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_path_params_list_items(self, async_client: AsyncKnock) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.feeds.with_raw_response.list_items(
                user_id="",
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.users.feeds.with_raw_response.list_items(
                user_id="user_id",
                id="",
            )
