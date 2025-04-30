# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from knockapi import Knock, AsyncKnock
from tests.utils import assert_matches_type
from knockapi.types.messages import (
    BatchArchiveResponse,
    BatchUnarchiveResponse,
    BatchGetContentResponse,
    BatchMarkAsReadResponse,
    BatchMarkAsSeenResponse,
    BatchMarkAsUnreadResponse,
    BatchMarkAsUnseenResponse,
    BatchMarkAsInteractedResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_archive(self, client: Knock) -> None:
        batch = client.messages.batch.archive(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )
        assert_matches_type(BatchArchiveResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_archive(self, client: Knock) -> None:
        response = client.messages.batch.with_raw_response.archive(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchArchiveResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_archive(self, client: Knock) -> None:
        with client.messages.batch.with_streaming_response.archive(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchArchiveResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_get_content(self, client: Knock) -> None:
        batch = client.messages.batch.get_content(
            message_ids=["string"],
        )
        assert_matches_type(BatchGetContentResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_get_content(self, client: Knock) -> None:
        response = client.messages.batch.with_raw_response.get_content(
            message_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchGetContentResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_get_content(self, client: Knock) -> None:
        with client.messages.batch.with_streaming_response.get_content(
            message_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchGetContentResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_mark_as_interacted(self, client: Knock) -> None:
        batch = client.messages.batch.mark_as_interacted(
            message_ids=["1jNaXzB2RZX3LY8wVQnfCKyPnv7"],
        )
        assert_matches_type(BatchMarkAsInteractedResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_mark_as_interacted_with_all_params(self, client: Knock) -> None:
        batch = client.messages.batch.mark_as_interacted(
            message_ids=["1jNaXzB2RZX3LY8wVQnfCKyPnv7"],
            metadata={"key": "bar"},
        )
        assert_matches_type(BatchMarkAsInteractedResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_mark_as_interacted(self, client: Knock) -> None:
        response = client.messages.batch.with_raw_response.mark_as_interacted(
            message_ids=["1jNaXzB2RZX3LY8wVQnfCKyPnv7"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchMarkAsInteractedResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_mark_as_interacted(self, client: Knock) -> None:
        with client.messages.batch.with_streaming_response.mark_as_interacted(
            message_ids=["1jNaXzB2RZX3LY8wVQnfCKyPnv7"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchMarkAsInteractedResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_mark_as_read(self, client: Knock) -> None:
        batch = client.messages.batch.mark_as_read(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )
        assert_matches_type(BatchMarkAsReadResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_mark_as_read(self, client: Knock) -> None:
        response = client.messages.batch.with_raw_response.mark_as_read(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchMarkAsReadResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_mark_as_read(self, client: Knock) -> None:
        with client.messages.batch.with_streaming_response.mark_as_read(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchMarkAsReadResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_mark_as_seen(self, client: Knock) -> None:
        batch = client.messages.batch.mark_as_seen(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )
        assert_matches_type(BatchMarkAsSeenResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_mark_as_seen(self, client: Knock) -> None:
        response = client.messages.batch.with_raw_response.mark_as_seen(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchMarkAsSeenResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_mark_as_seen(self, client: Knock) -> None:
        with client.messages.batch.with_streaming_response.mark_as_seen(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchMarkAsSeenResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_mark_as_unread(self, client: Knock) -> None:
        batch = client.messages.batch.mark_as_unread(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )
        assert_matches_type(BatchMarkAsUnreadResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_mark_as_unread(self, client: Knock) -> None:
        response = client.messages.batch.with_raw_response.mark_as_unread(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchMarkAsUnreadResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_mark_as_unread(self, client: Knock) -> None:
        with client.messages.batch.with_streaming_response.mark_as_unread(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchMarkAsUnreadResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_mark_as_unseen(self, client: Knock) -> None:
        batch = client.messages.batch.mark_as_unseen(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )
        assert_matches_type(BatchMarkAsUnseenResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_mark_as_unseen(self, client: Knock) -> None:
        response = client.messages.batch.with_raw_response.mark_as_unseen(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchMarkAsUnseenResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_mark_as_unseen(self, client: Knock) -> None:
        with client.messages.batch.with_streaming_response.mark_as_unseen(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchMarkAsUnseenResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_unarchive(self, client: Knock) -> None:
        batch = client.messages.batch.unarchive(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )
        assert_matches_type(BatchUnarchiveResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_unarchive(self, client: Knock) -> None:
        response = client.messages.batch.with_raw_response.unarchive(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchUnarchiveResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_unarchive(self, client: Knock) -> None:
        with client.messages.batch.with_streaming_response.unarchive(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchUnarchiveResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_archive(self, async_client: AsyncKnock) -> None:
        batch = await async_client.messages.batch.archive(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )
        assert_matches_type(BatchArchiveResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.batch.with_raw_response.archive(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchArchiveResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.batch.with_streaming_response.archive(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchArchiveResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_get_content(self, async_client: AsyncKnock) -> None:
        batch = await async_client.messages.batch.get_content(
            message_ids=["string"],
        )
        assert_matches_type(BatchGetContentResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_get_content(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.batch.with_raw_response.get_content(
            message_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchGetContentResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_get_content(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.batch.with_streaming_response.get_content(
            message_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchGetContentResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_mark_as_interacted(self, async_client: AsyncKnock) -> None:
        batch = await async_client.messages.batch.mark_as_interacted(
            message_ids=["1jNaXzB2RZX3LY8wVQnfCKyPnv7"],
        )
        assert_matches_type(BatchMarkAsInteractedResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_mark_as_interacted_with_all_params(self, async_client: AsyncKnock) -> None:
        batch = await async_client.messages.batch.mark_as_interacted(
            message_ids=["1jNaXzB2RZX3LY8wVQnfCKyPnv7"],
            metadata={"key": "bar"},
        )
        assert_matches_type(BatchMarkAsInteractedResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_mark_as_interacted(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.batch.with_raw_response.mark_as_interacted(
            message_ids=["1jNaXzB2RZX3LY8wVQnfCKyPnv7"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchMarkAsInteractedResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_mark_as_interacted(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.batch.with_streaming_response.mark_as_interacted(
            message_ids=["1jNaXzB2RZX3LY8wVQnfCKyPnv7"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchMarkAsInteractedResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_mark_as_read(self, async_client: AsyncKnock) -> None:
        batch = await async_client.messages.batch.mark_as_read(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )
        assert_matches_type(BatchMarkAsReadResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_mark_as_read(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.batch.with_raw_response.mark_as_read(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchMarkAsReadResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_mark_as_read(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.batch.with_streaming_response.mark_as_read(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchMarkAsReadResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_mark_as_seen(self, async_client: AsyncKnock) -> None:
        batch = await async_client.messages.batch.mark_as_seen(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )
        assert_matches_type(BatchMarkAsSeenResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_mark_as_seen(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.batch.with_raw_response.mark_as_seen(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchMarkAsSeenResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_mark_as_seen(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.batch.with_streaming_response.mark_as_seen(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchMarkAsSeenResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_mark_as_unread(self, async_client: AsyncKnock) -> None:
        batch = await async_client.messages.batch.mark_as_unread(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )
        assert_matches_type(BatchMarkAsUnreadResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_mark_as_unread(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.batch.with_raw_response.mark_as_unread(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchMarkAsUnreadResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_mark_as_unread(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.batch.with_streaming_response.mark_as_unread(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchMarkAsUnreadResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_mark_as_unseen(self, async_client: AsyncKnock) -> None:
        batch = await async_client.messages.batch.mark_as_unseen(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )
        assert_matches_type(BatchMarkAsUnseenResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_mark_as_unseen(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.batch.with_raw_response.mark_as_unseen(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchMarkAsUnseenResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_mark_as_unseen(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.batch.with_streaming_response.mark_as_unseen(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchMarkAsUnseenResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_unarchive(self, async_client: AsyncKnock) -> None:
        batch = await async_client.messages.batch.unarchive(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )
        assert_matches_type(BatchUnarchiveResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_unarchive(self, async_client: AsyncKnock) -> None:
        response = await async_client.messages.batch.with_raw_response.unarchive(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchUnarchiveResponse, batch, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_unarchive(self, async_client: AsyncKnock) -> None:
        async with async_client.messages.batch.with_streaming_response.unarchive(
            message_ids=["2w3YUpTTOxuDvZFji8OMsKrG176", "2w3YVRbPXMIh8Zq6oBFcVDA5xes"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchUnarchiveResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True
